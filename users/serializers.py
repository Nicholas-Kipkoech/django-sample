from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
       model = User
       fields=['id','first_name','last_name','password']


    def create(self,data):
           password = data.pop('password')
           instance = self.Meta.model(**data)
           instance.set_password(password)
           instance.save()
           return instance


