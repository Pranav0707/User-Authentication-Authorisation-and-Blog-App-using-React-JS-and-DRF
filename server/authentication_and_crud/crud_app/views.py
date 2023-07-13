from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from crud_app.serializers import BlogSerializer
from . import custom_permissions
from rest_framework.authentication import SessionAuthentication
from .models import Blog
from django.contrib.auth.models import User
from django.utils.functional import SimpleLazyObject
from rest_framework import status

class BlogView(APIView):

    # permission_classes=(IsAuthenticated,custom_permissions.IsOwnerOrReadOnly)

    def get(self, request):
        author=Blog.objects.filter(author=request.user)
        print(request.user)
        serializer=BlogSerializer(instance=author,many=True)
        return Response(serializer.data)

    def post(self, request):

        # data = {
        #     "author": request.user,
        #     "title": request.data.get('title', None),
        #     "description": request.data.get('description', None),
        #     "content": request.data.get('content', None),
        #     "image": request.data.get('image', None)
        # }
        try:
            obj = Blog.objects.create(author=request.user,
                                        title=request.data.get('title', None),
                                        description=request.data.get(
                                            'description', None),
                                        content=request.data.get('content', None),
                                        image=request.data.get('image', None))
            
            obj.save()

            serializer=BlogSerializer(instance=obj)
            return  Response({
            "message":"Blog Saved Successfully",
            "response":serializer.data,
            },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error":'error occured'},status=status.HTTP_400_BAD_REQUEST)
        

class AllBlogs(APIView):
    def get(self,request):
        blogs=Blog.objects.all()
        # print(blogs)
        serializer=BlogSerializer(instance=blogs,many=True)
        return Response(serializer.data)