from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
# @login_required(login_url='login')
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            auth_login(request,user)
            return redirect('profile')
        else:
                return HttpResponse ("Username or Password is incorrect!!!")
    return render (request,'login.html')

def logout(request):
    return redirect('login')

def profile(request):
    if request.method =='POST':             
                name=request.POST.get('name','')
                email=request.POST.get('email','')
                phone=request.POST.get('phone','')
                gender=request.POST.get('gender','') 
                address=request.POST.get('address','')       
                city=request.POST.get('city','')
                state=request.POST.get('state','')
                profile = Profile(name=name, email=email, phone=phone, gender=gender, address=address, city=city, state=state)
                profile.save()
    return render(request,'profile.html')


