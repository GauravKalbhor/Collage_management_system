from django.shortcuts import render
from django.http import  HttpResponse
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render (request,'app/home.html')

def adminLogin(request):
    if request.method == "POST":
        adminID = request.POST['adminID']
        adminPassword = request.POST['adminPassword']
        
        id = 'admin@gmail.com'
        password = 'admin$1234'
        # data = AdminLogin.objects.filter(id=adminID)
        if (id==adminID and password==adminPassword):
            # login_data = AdminLogin.objects.get(id=adminID)
            
            if password == adminPassword:
                return render(request,'app/home.html')
            else:
                message = "Email id or Password Not match"
                return render(request,'admin/adminLogin.html',{'msg':message})
        else:
            form = Admin_form()
            return render(request,'admin/adminLogin.html',{'form':form,'msg':message})
    else:
        form = Admin_form()
        return render(request,'admin/adminLogin.html',{'form':form})
