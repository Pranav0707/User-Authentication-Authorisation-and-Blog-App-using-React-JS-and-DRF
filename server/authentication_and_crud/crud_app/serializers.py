from rest_framework import serializers
from django.contrib.auth.models import User
from crud_app.models import Blog


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=["id","username","email"]

class BlogSerializer(serializers.ModelSerializer):
    author=UserSerializer(read_only=True)
    class Meta:
        model = Blog
        fields=["title","description","content","image","author"]
        extra_kwargs={
            'author':{'allow_null':True,'required':False}
        }

       