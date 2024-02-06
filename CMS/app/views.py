from django.shortcuts import render
from django.http import  HttpResponse
from .models import *
from .forms import *

# Create your views here.


def home(request):
    return render (request,'app/home.html')

def adminDashbord(request):
    stu_count = Stu_FormDetails.objects.count()
    teach_count = Teach_FormDetails.objects.count()
    data ={
                'stu_count':stu_count,
                'teach_count':teach_count,
            }
    return render (request,'admin/admin_dashboard.html',{'data':data})

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
    

def studentLogin(request):
    if request.method == "POST":
        student_email = request.POST['email']
        student_password = request.POST['password']

        stu_data = Stu_FormDetails.objects.filter(stu_Email = student_email)
        if stu_data:
            data = Stu_FormDetails.objects.get(stu_Email = student_email)
            if (data.stu_ID == student_password):
                return render(request,'student/student_dashboard.html')
            else:
                message = "Email or Password are not valid"
                return render(request,'student/studenLogin.html',{'msg':message})
    return render(request,'student/studentLogin.html')

def student_add(request):
    if request.method =="POST":
        stu_ID = request.POST['stuID']
        stu_Name=request.POST['fullname']
        stu_faName=request.POST['fathername']
        dob=request.POST['dob']
        dobjob=request.POST['dobjob']
        add=request.POST['add']
        email=request.POST['email']
        mobile=request.POST['mobile']
        emmobile=request.POST['emmobile']
        adhar=request.POST['adhar']
        gender=request.POST['gender']
        graduation=request.POST['graduation']
        branch=request.POST['branch']
        collage=request.POST['collage']
        department=request.POST['department']
        course=request.POST['course']
        stu = Stu_FormDetails.objects.filter(stu_Email=email)
        if stu:
            msg="Student is already exist, Submit next student data"
            stu_count = Stu_FormDetails.objects.count()
            teach_count = Teach_FormDetails.objects.count()
            data ={'stu_count':stu_count,'teach_count':teach_count,'msg':msg}
            return render(request, 'admin/student_add.html',{'data':data})
        else:
            Stu_FormDetails.objects.create(stu_ID = stu_ID,
 stu_Name=stu_Name,stu_FaName=stu_faName,stu_DOB=dob,stu_DOBjob=dobjob,
stu_Add=add,stu_Email=email,stu_Mobile=mobile,stu_EmMobile=emmobile,
stu_Adhar=adhar,stu_Gender=gender,stu_Graduation=graduation,
stu_Branch=branch,stu_Collage=collage,stu_Department=department,stu_Course= course)
            msg= "Student register"
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
        return render (request,'admin/student_add.html',{'data':data})
    

def student_showData(request):
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
    return render(request,'admin/student_showData.html',{'data':data})

def teacher_add (request):
    if request.method =="POST":
        teachID = request.POST['teachID']
        jtitle=request.POST['jtitle']
        fullname=request.POST['fullname']
        dob=request.POST['dob']
        dobjob=request.POST['dobjob']
        department=request.POST['department']
        course=request.POST['course']
        faname=request.POST['faname']
        email=request.POST['email']
        mobile=request.POST['mobile']
        emmobile=request.POST['emmobile']
        graduation=request.POST['graduation']
        postgraduation=request.POST['postgraduation']
        adhar=request.POST['adhar']
        add=request.POST['add']
        gender=request.POST['gender']
        tech = Teach_FormDetails.objects.filter(teach_Email=email)
        if tech:
            msg="Teacher is already exist, Submit next Teacher data"
            stu_count = Stu_FormDetails.objects.count()
            teach_count = Teach_FormDetails.objects.count()
            data ={'stu_count':stu_count,'teach_count':teach_count,'msg':'msg'}
            return render(request, 'admin/teacher_add.html',{'data':data})
        else:
            Teach_FormDetails.objects.create(teach_ID = teachID,teach_jtitle=jtitle,
teach_Name=fullname,teach_DOB=dob,teach_DOBjob=dobjob,teach_Department=department,
teach_Course= course,teach_FaName=faname,teach_Email=email, teach_Mobile= mobile,
teach_EmMobile=emmobile,teach_Graduation=graduation,teach_Postgraduation=postgraduation,
teach_Adhar=adhar,teach_Add=add,teach_Gender=gender)
            msg= "Teacher register"
            stu_count = Stu_FormDetails.objects.count()
            teach_count = Teach_FormDetails.objects.count()
            data ={
                'stu_count':stu_count,
                'teach_count':teach_count,
                'msg':msg
            }
            return render(request, 'admin/teacher_add.html',{'data':data})
    else :
        stu_count = Stu_FormDetails.objects.count()
        teach_count = Teach_FormDetails.objects.count()
        data ={
            'stu_count':stu_count,
            'teach_count':teach_count,
        }
        return render(request, 'admin/teacher_add.html',{'data':data})



def teacher_showData(request):
    dataAll = Teach_FormDetails.objects.all()
    msg="Student is already exist, Submit next student data"
    stu_count = Stu_FormDetails.objects.count()
    teach_count = Teach_FormDetails.objects.count()
    data ={
            'stu_count':stu_count,
            'teach_count':teach_count,
            'msg':msg,
            'dataAll':dataAll
            }    
    return render(request,'admin/teacher_showData.html',{'data':data})

def student_view(request):
    return render(request,"admin/student_view.html")