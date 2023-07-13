from crud_app.views import BlogView,AllBlogs
from django.urls import path
urlpatterns = [
    path('',BlogView.as_view()),
    path('allBlogs/',AllBlogs.as_view())
]
