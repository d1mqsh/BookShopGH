from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Book




class UserSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        
        fields = ['id', 'username']



class BookSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Book
        
        fields = ['id','name', 'price']


