
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Car_Type(models.Model):
    name=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    
    def __self__(self):
        return self.cartype
    

# MODEL_CHOISES=(
#     ('S', 'Suv'),
#     ('C', 'Coupe')
# )

class Car(models.Model):
    name=models.CharField(max_length=50)
    img=models.CharField(max_length=500)
    year=models.IntegerField()
    country=models.CharField(max_length=50)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering =['name'] #search option