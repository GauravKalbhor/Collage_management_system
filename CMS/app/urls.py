from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name='home'),
    # admin 
    path("adminLogin/",adminLogin,name='adminLogin'),
    path("adminDashbord/",adminDashbord,name='adminDashbord'),
    # student 
    path("studentLogin/",studentLogin,name='studentLogin'),
    path("student_add/",student_add,name='student_add'),
    path("showData/",student_showData,name='student_showData'),
    path("student_dashboard/",student_dashboard,name='student_dashboard'),
    path("student_view/<int:id>/",student_view,name="student_view"),
    path("student_delete/<int:id>/",student_delete,name="student_delete"),
    path("student_editData/",student_editData,name='student_editData'),
    # teacher
    path("teacher_add/",teacher_add,name='teacher_add'),
    path("teacher_showData/",teacher_showData,name='teacher_showData'),
    path("teacher_view/<int:id>/",teacher_view,name='teacher_view'),
]