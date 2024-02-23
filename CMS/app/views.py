from django.shortcuts import render,redirect
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
        user = "Prashant Sir"
        if (admin_data['id'] == ad_ID and admin_data['password'] == ad_pass):
            return render(request,'admin/admin_dashboard.html',{'user':user})
        else:
            admin_form = Admin_form()
            return render(request,'admin/adminLogin.html',{'form':admin_form})
    else:    
        admin_form = Admin_form()
        return render(request,'admin/adminLogin.html',{'form':admin_form})

# all code related to student

def studentLogin(request):
    if request.method == "POST":
        student_email = request.POST['email']
        student_password = request.POST['password']

        stu_data = Stu_FormDetails.objects.filter(stu_Email = student_email)
        if stu_data:
            data = Stu_FormDetails.objects.get(stu_Email = student_email)
            if (data.stu_ID == student_password):
                name = data.stu_Name
                return render(request,'student/student_dashboard.html',{'stu_name':name})
            else:
                message = "Email or Password are not valid"
                return render(request,'student/studentLogin.html',{'msg':message})
    return render(request,'student/studentLogin.html')

def student_dashboard(request):
    return render(request,'student/studenLogin.html')

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
        course_fee=request.POST['fees']
        image = request.POST['image']
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
stu_Branch=branch,stu_Collage=collage,stu_Department=department,stu_Course= course,stu_Course_Fee=course_fee,stu_image=image)
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
        return render (request,'admin/student_add.html')
    

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


def student_view(request, id):
    view = Stu_FormDetails.objects.get(pk=id)
    print(view)
    stu_Id = view.stu_ID
    stu_Name = view.stu_Name
    stu_FaName = view.stu_FaName
    stu_DOB = view.stu_DOB
    stu_DOBjob = view.stu_DOBjob
    stu_Add = view.stu_Add
    stu_Email = view.stu_Email
    stu_Mobile = view.stu_Mobile
    stu_EmMobile = view.stu_EmMobile
    stu_Adhar = view.stu_Adhar
    stu_Gender=view.stu_Gender
    stu_Graduation=view.stu_Graduation
    stu_Branch=view.stu_Branch
    stu_Collage=view.stu_Collage
    stu_Department=view.stu_Department
    stu_Course=view.stu_Course
    stu_image = view.stu_image
    stu_Course_Fee = view.stu_Course_Fee

    global student_allData
    student_allData={
        'stu_Id':stu_Id,
        'stu_Name' :stu_Name,
        'stu_FaName' :stu_FaName,
        'stu_DOB' :stu_DOB,
        'stu_DOBjob' :stu_DOBjob,
        'stu_Add' :stu_Add,
        'stu_Email' :stu_Email,
        'stu_Mobile' :stu_Mobile,
        'stu_EmMobile' :stu_EmMobile,
        'stu_Adhar' :stu_Adhar,
        'stu_Gender':stu_Gender,
        'stu_Graduation':stu_Graduation,
        'stu_Branch':stu_Branch,
        'stu_Collage':stu_Collage,
        'stu_Department':stu_Department,
        'stu_Course':stu_Course,
        'stu_image' : stu_image,
        'stu_Course_Fee' : stu_Course_Fee
    }
    return render(request,"admin/student_view.html",{'student':student_allData})

def student_delete(request,id):
    delete_data = Stu_FormDetails.objects.get(pk=id)
    print(delete_data)
    delete_data.delete()
    stu_Id = delete_data.stu_ID
    stu_Name = delete_data.stu_Name
    stu_FaName = delete_data.stu_FaName
    stu_DOB = delete_data.stu_DOB
    stu_DOBjob = delete_data.stu_DOBjob
    stu_Add = delete_data.stu_Add
    stu_Email = delete_data.stu_Email
    stu_Mobile = delete_data.stu_Mobile
    stu_EmMobile = delete_data.stu_EmMobile
    stu_Adhar = delete_data.stu_Adhar
    stu_Gender=delete_data.stu_Gender
    stu_Graduation=delete_data.stu_Graduation
    stu_Branch=delete_data.stu_Branch
    stu_Collage=delete_data.stu_Collage
    stu_Department=delete_data.stu_Department
    stu_Course=delete_data.stu_Course
    stu_image = delete_data.stu_image
    stu_Course_Fee = delete_data.stu_Course_Fee

    student_deleteData={
        'stu_Id':stu_Id,
        'stu_Name' :stu_Name,
        'stu_FaName' :stu_FaName,
        'stu_DOB' :stu_DOB,
        'stu_DOBjob' :stu_DOBjob,
        'stu_Add' :stu_Add,
        'stu_Email' :stu_Email,
        'stu_Mobile' :stu_Mobile,
        'stu_EmMobile' :stu_EmMobile,
        'stu_Adhar' :stu_Adhar,
        'stu_Gender':stu_Gender,
        'stu_Graduation':stu_Graduation,
        'stu_Branch':stu_Branch,
        'stu_Collage':stu_Collage,
        'stu_Department':stu_Department,
        'stu_Course':stu_Course,
        'stu_image' : stu_image,
        'stu_Course_Fee' : stu_Course_Fee
    }
    dataAll = Stu_FormDetails.objects.all()
    messages = "Student data delete successfully"
    return render(request,"admin/student_showData.html",{'student':student_deleteData,'data':dataAll,'msg':messages})

def student_editData(request):
    return render(request,'admin/student_editData.html')

#  all code related to teacher

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

def teacher_view(request,id):
    view = Teach_FormDetails.objects.get(pk=id)
    print(view)
    teach_ID = view.teach_ID
    teach_jtitle = view.teach_jtitle
    teach_Name = view.teach_Name
    teach_DOB = view.teach_DOB
    teach_DOBjob = view.teach_DOBjob
    teach_Department = view.teach_Department
    teach_Course = view.teach_Course
    teach_FaName = view.teach_FaName
    teach_Email = view.teach_Email
    teach_Mobile = view.teach_Mobile
    teach_EmMobile = view.teach_EmMobile
    teach_Graduation = view.teach_Graduation
    teach_Postgraduation = view.teach_Postgraduation
    teach_Adhar = view.teach_Adhar
    teach_Add = view.teach_Add
    teach_Gender = view.teach_Gender

    teach_allData = {
        'teach_ID' : teach_ID,
        'teach_jtitle' : teach_jtitle,
        'teach_Name' : teach_Name,
        'teach_DOB' : teach_DOB,
        'teach_DOBjob' : teach_DOBjob,
        'teach_Department' : teach_Department,
        'teach_Course' : teach_Course,
        'teach_FaName' : teach_FaName,
        'teach_Email' : teach_Email,
        'teach_Mobile' : teach_Mobile,
        'teach_EmMobile' : teach_EmMobile,
        'teach_Graduation' : teach_Graduation,
        'teach_Postgraduation' : teach_Postgraduation,
        'teach_Adhar' : teach_Adhar,
        'teach_Add' : teach_Add,
        'teach_Gender' : teach_Gender,
    }
    return render(request,'admin/teacher_view.html',{'teacher':teach_allData})

def teach_deleteData(request,id):
    delete_data = Teach_FormDetails.objects.get(pk=id)

    teach_ID = delete_data.teach_ID
    teach_jtitle = delete_data.teach_jtitle
    teach_Name = delete_data.teach_Name
    teach_DOB = delete_data.teach_DOB
    teach_DOBjob = delete_data.teach_DOBjob
    teach_Department = delete_data.teach_Department
    teach_Course = delete_data.teach_Course
    teach_FaName = delete_data.teach_FaName
    teach_Email = delete_data.teach_Email
    teach_Mobile = delete_data.teach_Mobile
    teach_EmMobile = delete_data.teach_EmMobile
    teach_Graduation = delete_data.teach_Graduation
    teach_Postgraduation = delete_data.teach_Postgraduation
    teach_Adhar = delete_data.teach_Adhar
    teach_Add = delete_data.teach_Add
    teach_Gender = delete_data.teach_Gender

    teach_deleteData = {
        'teach_ID' : teach_ID,
        'teach_jtitle' : teach_jtitle,
        'teach_Name' : teach_Name,
        'teach_DOB' : teach_DOB,
        'teach_DOBjob' : teach_DOBjob,
        'teach_Department' : teach_Department,
        'teach_Course' : teach_Course,
        'teach_FaName' : teach_FaName,
        'teach_Email' : teach_Email,
        'teach_Mobile' : teach_Mobile,
        'teach_EmMobile' : teach_EmMobile,
        'teach_Graduation' : teach_Graduation,
        'teach_Postgraduation' : teach_Postgraduation,
        'teach_Adhar' : teach_Adhar,
        'teach_Add' : teach_Add,
        'teach_Gender' : teach_Gender,
    }
    return render(request,'admin/teacher_view.html',{'teacher_delete':teach_deleteData})