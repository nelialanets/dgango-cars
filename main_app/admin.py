from django.contrib import admin

from .models import Car, Car_Type#importing car model from models
# Register your models here.

admin.site.register(Car)
admin.site.register(Car_Type)
