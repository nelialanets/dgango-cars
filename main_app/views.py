from asyncio import subprocess
from dataclasses import field
from email.mime import audio
from nis import cat
from re import template
from urllib import response
from wsgiref.util import request_uri
from django.http import HttpResponse, HttpResponseRedirect # responses 
from django.shortcuts import render
from django.views import View 
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from .models import Car
from .models import Car_Type
from  django.contrib.auth.models import User
# Auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


class Home(TemplateView):
   template_name= 'home.html'

class About(TemplateView):
    template_name ='about.html'


class Car_List(TemplateView):
    template_name ='cars.html'


# class Car:

#     def __init__(self, name, year, country):
#         self.name =name,
#         self.year=year,
#         self.country = country

# cars=[
#     Car('BMW M1', 2022, 'Germany'),
#     Car('BMW M2', 2022, 'Germany'),
#     Car('BMW M3', 2022, 'Germany'),
#     Car('BMW M4', 2022, 'Germany'),
#     Car('BMW M2', 2022, 'Germany'),
#     Car('Mercedes 63 AMG',  2022, 'Germany'),
#     Car('Mercedes S550 AMG',  2022, 'Germany'),
#     Car('Mercedes  E400 AMG',  2022, 'Germany'),
# ]

#(CRUD)

class Car_List(TemplateView):
    template_name= 'cars.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object
        context['cars']=Car.objects.all 
        name= self.request.GET.get('name')
        if name !=None:
            context['cars']=Car.objects.filter(name__icontains=name)
            context['header'] = f"Searching for {name}"
        else:
            context["cars"] = Car.objects.all()
            context ['header']='Cars List'
        return context

        # CREATE 
@method_decorator(login_required, name='dispatch')
class Car_Create(CreateView):
    model=Car
    fields=['name', 'img', 'year', 'country', 'user']
    template_name ='create_car.html'
    success_url = '/cars/' #redirect to /cars 
    def get_success_url(self):
      return reverse('car_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.user = self.request.user# wehn we  make a request for the user that comes with the form of the created car== it will show who created a car 
        return HttpResponseRedirect('/cars')

@method_decorator(login_required, name='dispatch')
class Car_Detail(DetailView):
    model=Car
    template_name='car_detail.html'
    def get_success_url(self):
     return reverse('car_detail', kwargs={'pk': self.object.pk}) # looking by id

@method_decorator(login_required, name='dispatch')
class Car_Update(UpdateView):
    model=Car
    fields=['name', 'img', 'year', 'country']
    template_name ='car_update.html'
    def get_success_url(self):
     return reverse('car_detail', kwargs={'pk': self.object.pk}) 

@method_decorator(login_required, name='dispatch')
class Car_Delete(DeleteView):
    model=Car
    template_name="car_delete.html"
    success_url ='/cars/' #redirect 

@login_required
def Profile(request, username):
    user= User.objects.get(username=username)
    cars= Car.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'cars': cars}) #{'username': username, 'caars': cars})  key and a value

## CRUD for Car_Type
#index 


def Cartype_Index(request):
    cartypes= Car_Type.objects.all()# going to the cat_model to grab all of the car types in the db
    return render (request, 'cartypes_index.html',{ 'cartypes': cartypes })

def Cartype_Show(request, cartype_id):
    cartype=Car_Type.objects.get(id=cartype_id)
    return render (request, 'cartypes_show.html', {'cartype':cartype}) # rendering out cartype=Car_Type.objects.get(id=cartype_id) object
@method_decorator(login_required, name='dispatch')

class Cartype_Create(CreateView):
    model= Car_Type
    fields='__all__'
    template_name= "cartypes_create.html"
    success_url='/cartype'

@method_decorator(login_required, name='dispatch')
class Cartype_Update(UpdateView):
    mode=Car_Type
    fields=['name' 'color']
    template_field= 'cartypes_update.html'
    success_url='/cartype'


@method_decorator(login_required, name='dispatch')
class Cartype_Delete(DeleteView):
    model= Car_Type
    template_name= "cartypes_delete.html"
    success_url='/cartype'


#  AUTH


def login_view(request):
    # if POST then authentificate  the user (submitting user name and paswor)
    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user= authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('the acount has been disableled')
                    return HttpResponseRedirect('/login/')
            else:
                print('the username or passwork is incrrect')
    else:
        # user is going to the login page
        form=AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/cars')


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            print("hey", user.username)
            return HttpResponseRedirect('/user/' + str(user.username))
        else:
            HttpResponse('<h1>Try again</h1>')
    else:
        form=UserCreationForm()
        return render(request, 'signup.html', {'form':form})


