from django.urls import  path
from . import views

urlpatterns=[
path('', views.Home.as_view(), name='home'),
path('about/', views.About.as_view(), name = 'about'),
path('cars/', views.Car_List.as_view(), name = 'cars'),
path('cars/new/', views.Car_Create.as_view(), name='create_car'),
path('cars/<int:pk>/', views.Car_Detail.as_view(), name='car_detail'), #show page
path('cars/<int:pk>/update', views.Car_Update.as_view(), name='car_update'),
path('cars/<int:pk>delete', views.Car_Delete.as_view(), name='car_delete'),
path('user/<username>/', views.Profile, name='profile'),
######Car_Type CRUD########
path('cartype/', views.Cartype_Index, name="cartypes_index"),
path('cartypes/<int:cartypes_id>', views.Cartype_Show, name="cartypes_show"),
path('cartypes/create/', views.Cartype_Create.as_view(), name="cartypes_create"),
path('cartypes/<int:pk>/update', views.Cartype_Update.as_view(), name="cartypes_update"),
path('cartypes/<int:pk>/delete', views.Cartype_Delete.as_view(), name="cartypes_delete"),

# Auath
path('login/', views.Login_view, name='login'),
path('logout/', views.Logout_view, name='logout'),
path('signup/', views.Sighup_view, name='sighup'),

]