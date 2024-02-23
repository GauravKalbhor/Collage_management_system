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
    
    adminPassword = forms.CharField(widget=forms.PasswordInput())
    def clean_adminPassword(self):
        adminPass = self.cleaned_data["adminPassword"]
        password = 'admin$1234'
        if len(adminPass)==password:
            raise forms.ValidationError('Password not exist')
        return adminPass
    
# class StudentAddForm(forms.ModelForm):
#     class Meta :
#         model = Stu_Details
#         fields = "__all__"
