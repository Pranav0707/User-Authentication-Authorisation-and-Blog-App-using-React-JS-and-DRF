from django.urls import path,include
from . views import RegisterView,LoginView,UserView,UserLogoutView
urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('userData/',UserView.as_view()),
    path('logout/',UserLogoutView.as_view())
]