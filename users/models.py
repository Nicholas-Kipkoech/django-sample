from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=200,blank=True,null=True)
    last_name=models.CharField(max_length=200,blank=True,null=True)
    password=models.CharField(max_length=200)

    def __str__(self):
        return f"Name: {self.first_name}"
    

    def set_password(self,raw_password):
        self.password=make_password(raw_password)


    
   


