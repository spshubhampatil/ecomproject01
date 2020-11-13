from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from shop.models.user import User
from django.shortcuts import render, HttpResponse, redirect

class SignupView(View):
    def get(self, request):
        return render(request,'signup.html')
        
    def post(self, request):
        thank=False
        try:
            fname=request.POST.get('fname')
            print(fname)
            lname=request.POST.get('lname')
            print(lname)
            email=request.POST.get('email')
            print(email)
            password=request.POST.get('password')
            print(password)
            dob=request.POST.get('dob')
            print(dob)
            hashedpassword=make_password(password=password)
            user= User(name=fname, email=email,password=hashedpassword,dob=dob)
            print(user)
            user.save()           
            thank=True   
            return render(request,'login.html',{'thank':thank})
        except:
            return render(request,'signup.html',{'error':"User already existed..."})

