from django.urls import path
from .views import *
urlpatterns = [
    path("",home,name='home'),
    path("adminLogin/",adminLogin,name='adminLogin'),
    path("studentLogin/",studentLogin,name='studentLogin'),
    path("adminDashbord/",adminDashbord,name='adminDashbord'),
    path("student_add/",student_add,name='student_add'),
    path("showData/",student_showData,name='showData'),
    path("teacher_add/",teacher_add,name='teacher_add'),
    # path("student/",student,name='student')
    # path("student_add/",student_add,name='student_add'),
    path("teacher_showData/",teacher_showData,name='teacher_showData'),
]