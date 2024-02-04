from django.shortcuts import render
from django.http import  HttpResponse
from .models import *
from .forms import *

# Create your views here.


def home(request):
    return render (request,'app/home.html')
def adminDashbord(request):
    return render (request,'admin/admin_dashboard.html')

def adminLogin(request):
    if request.method == "POST":
        ad_ID = request.POST['adminID']
        ad_pass = request.POST['adminPassword']

        admin_data = {
            'id' : 'admin@cybrom.co.in',
            'password' : 'admin@1234'
        }
        if (admin_data['id'] == ad_ID and admin_data['password'] == ad_pass):
            return render(request,'admin/admin_dashboard.html')
        else:
            admin_form = Admin_form()
            return render(request,'admin/adminLogin.html',{'form':admin_form})
    else:    
        admin_form = Admin_form()
        return render(request,'admin/adminLogin.html',{'form':admin_form})
    

def student_add (request):
    if request.method =="POST":
        stu_ID = request.POST['stuID']
        stu_Name=request.POST['fullname']
        fatherName=request.POST['fatherName']
        dob=request.POST['dob']
        email=request.POST['email']
        mobile=request.POST['mobile']
        address=request.POST['address']
        gender=request.POST['gender']
        cast=request.POST['cast']
        qualification=request.POST['qualification']
        department=request.POST['department']
        course=request.POST['course']

        Stu_Details.objects.create(stu_ID = stu_ID,
 stu_Name=stu_Name, stu_FatherName = fatherName,
 stu_DOB=dob, stu_Email=email, stu_Mobile= mobile,
stu_Address=address,stu_Gender=gender,stu_Cast=cast,
stu_Department=department, stu_Qualification=qualification,
stu_Course= course)
        return render(request, 'admin/student_add.html')
    else :
        return render(request, 'admin/student_add.html')





