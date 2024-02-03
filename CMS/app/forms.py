from django import forms
from .models import *

class Admin_form(forms.ModelForm):
    class Meta:
        model = AdminLogin
        fields = '__all__'

    def clean_adminID(self):
        adminID = self.cleaned_data["adminID"]
        id = 'admin@gmail.com'
        if len(adminID)==id:
            raise forms.ValidationError('Enter a valid id')
        return adminID
    
    def clean_adminPassword(self):
        adminPass = self.cleaned_data["adminPassword"]
        password = 'admin$1234'
        if len(adminPass)==password:
            raise forms.ValidationError('Password not exist')
        return adminPass
    


class Student_Form(forms.ModelForm):
    class Meta:
        model = Stu_Details()
        fields = "__all__"

    def clean_stu_FistName(self):
        FirstName = self.cleaned_data["stu_FistName"]
        if len(FirstName)<=2:
            raise forms.ValidationError('Enter Your First Name')
        return FirstName

    def clean_stu_LastName(self):
        LastName = self.cleaned_data["stu_LastName"]
        if len(LastName)<=2:
            raise forms.ValidationError('Enter Your Last Name')
        return LastName

    def clean_stu_RollNo(self):
        RollNo = self.cleaned_data["stu_RollNo"]
        if len(RollNo)<=8:
            raise forms.ValidationError('Roll no must 8 or more character')
        return RollNo

    def clean_stu_Email(self):
        Email = self.cleaned_data["stu_Email"]
        if len(Email)<=8:
            raise forms.ValidationError('Email must 8 or more than 8 character')
        return Email

    def clean_stu_Contact(self):
        Contact = self.cleaned_data["stu_Contact"]
        if Contact != 10:
            raise forms.ValidationError('Enter correct contact')
        return Contact

    def clean_stu_Fee(self):
        Fee = self.cleaned_data["stu_Fee"]
        if Fee < 2000:
            raise forms.ValidationError('Enter Fees')
        return Fee

    def clean_stu_Course(self):
        Course = self.cleaned_data["stu_Course"]
        if len(Course)<=5:
            raise forms.ValidationError('Enter Your Name')
        return Course

    def clean_stu_Branch(self):
        Branch = self.cleaned_data["stu_Branch"]
        if len(Branch)<= 2:
            raise forms.ValidationError('Enter a Valid Branch')
        return Branch

    def clean_stu_Year(self):
        Year = self.cleaned_data["stu_Year"]
        if Year <=2:
            raise forms.ValidationError('Enter year must be ')
        return Year
    