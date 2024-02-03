from django.urls import path
from .views import *
urlpatterns = [
    path("",home,name='home'),
    path("adminLogin/",adminLogin,name='adminLogin'),
    path("student/",student,name='student')
]
