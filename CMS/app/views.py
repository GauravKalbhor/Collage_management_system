from django.shortcuts import render
from django.http import  HttpResponse
from .models import *
from .forms import *

# Create your views here.


def home(request):
    return render (request,'app/home.html')

def adminDashbord(request):
    return render (request,'admin/admin_dashboard.html',{"stu_count":stu_count})

def adminLogin(request):
    if request.method == "POST":
        ad_ID = request.POST['adminID']
        ad_pass = request.POST['adminPassword']

        admin_data = {
            'id' : 'admin@cybrom.co.in',
            'password' : 'admin@1234'
        }
        if (admin_data['id'] == ad_ID and admin_data['password'] == ad_pass):
            stu_count = Stu_FormDetails.objects.count()
            teach_count = Teach_FormDetails.objects.count()
            data ={
                'stu_count':stu_count,
                'teach_count':teach_count
            }
            return render(request,'admin/admin_dashboard.html',{"data":data})
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
        dob=request.POST['dob']
        email=request.POST['email']
        mobile=request.POST['mobile']
        gender=request.POST['gender']
        department=request.POST['department']
        course=request.POST['course']
        stu = Stu_FormDetails.objects.filter(stu_Email=email)
        if stu:
            msg="Student is already exist, Submit next student data"
            stu_count = Stu_FormDetails.objects.count()
            teach_count = Teach_FormDetails.objects.count()
            data ={
                'stu_count':stu_count,
                'teach_count':teach_count,
                'msg':msg
            }
            return render(request, 'admin/student_add.html',{'data':data})
        else:
            Stu_FormDetails.objects.create(stu_ID = stu_ID,
 stu_Name=stu_Name,stu_DOB=dob, stu_Email=email, 
 stu_Mobile= mobile,stu_Gender=gender,
stu_Department=department,stu_Course= course)
            msg= "Teacher register"
            stu_count = Stu_FormDetails.objects.count()
            teach_count = Teach_FormDetails.objects.count()
            data ={
                'stu_count':stu_count,
                'teach_count':teach_count,
                'msg':msg
            }
            return render(request, 'admin/student_add.html',{'data':data})
    else :
        stu_count = Stu_FormDetails.objects.count()
        teach_count = Teach_FormDetails.objects.count()
        data ={
                'stu_count':stu_count,
                'teach_count':teach_count,

            }
        return render(request, 'admin/student_add.html',{'data':data})

def showData(request):
    dataAll = Stu_FormDetails.objects.all()
    msg="Student is already exist, Submit next student data"
    stu_count = Stu_FormDetails.objects.count()
    teach_count = Teach_FormDetails.objects.count()
    data ={
            'stu_count':stu_count,
            'teach_count':teach_count,
            'msg':msg,
            'dataAll':dataAll
            }    
    return render(request,'admin/student_data.html',{'data':data})


# ---------------------------------------------------------------
def teacher_add (request):
    if request.method =="POST":
        teachID = request.POST['teachID']
        jtitle=request.POST['jtitle']
        fullname=request.POST['fullname']
        dob=request.POST['dob']
        email=request.POST['email']
        mobile=request.POST['mobile']
        gender=request.POST['gender']
        course=request.POST['course']
        tech = Teach_FormDetails.objects.filter(teach_Email=email)
        if tech:
            msg="Teacher is already exist, Submit next Teacher data"
            stu_count = Stu_FormDetails.objects.count()
            teach_count = Teach_FormDetails.objects.count()
            data ={
                'stu_count':stu_count,
                'teach_count':teach_count,
                'msg':'msg'
            }
            return render(request, 'teacher/teacher_add.html',{'data':data})
        else:
            Teach_FormDetails.objects.create(teach_ID = teachID,
teach_jtitle=jtitle, teach_Name=fullname,teach_DOB=dob,
teach_Email=email, teach_Mobile= mobile,teach_Gender=gender,
teach_Course= course)
            msg= "Teacher register"
            stu_count = Stu_FormDetails.objects.count()
            teach_count = Teach_FormDetails.objects.count()
            data ={
                'stu_count':stu_count,
                'teach_count':teach_count,
                'msg':msg
            }
            return render(request, 'teacher/teacher_add.html',{'data':data})
    else :
        stu_count = Stu_FormDetails.objects.count()
        teach_count = Teach_FormDetails.objects.count()
        data ={
            'stu_count':stu_count,
            'teach_count':teach_count,
        }
        return render(request, 'teacher/teacher_add.html',{'data':data})
    

def showTeacherData(request):
    dataAll = Teach_FormDetails.objects.all()    
    stu_count = Stu_FormDetails.objects.count()
    teach_count = Teach_FormDetails.objects.count()
    data ={
        'stu_count':stu_count,
        'teach_count':teach_count,
        'dataAll':dataAll
        }
    return render(request,'teacher/teacher_data.html',{'data':data})






