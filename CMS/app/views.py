from django.shortcuts import render
from django.http import  HttpResponse
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render (request,'app/home.html')

def adminLogin(request):
    if request.method == "POST":
        ad_ID = request.POST['adminID']
        ad_pass = request.POST['adminPassword']

        admin_data = {
            'id' : 'admin@cybrom.co.in',
            'password' : 'admin@1234'
        }
        if (admin_data['id'] == ad_ID and admin_data['password'] == ad_pass):
            return render(request,'app/home.html')
        else:
            admin_form = Admin_form()
            return render(request,'admin/adminLogin.html',{'form':admin_form})
    else:
        admin_form = Admin_form()
        return render(request,'admin/adminLogin.html',{'form':admin_form})
    
def student(request):
    if request.method == "POST":
        stu_data = Student_Form(request.POST)
        if stu_data.is_valid():
            stu_data.save()
            message = "Student details register successfully"
            stu_form = Student_Form()
            return render(request,'admin/adminLogin.html',{'stu_form':stu_form,'msg':message})
    else:
        stu_form = Student_Form()
    return render(request,'admin/adminLogin.html',{'stu_form':stu_form})
