from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import Edituserform

# Create your views here.
def signin(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            usname=request.POST['username']
            passw=request.POST['password']
            user=authenticate(request,username=usname,password=passw)
            if user is not None:
                login(request,user)
                return redirect('home')
        return render(request,'sign-in.html')
    else:
        return HttpResponse("You are already login")

def signup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['Username']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        if pass1!= pass2:
            return HttpResponse("Password Not Matched")
        else:
            my_user=User.objects.create_user(username=uname,email=email,first_name=fname,last_name=lname,password=pass1)
            my_user.save()
            return redirect('/')
    return render(request,'signup.html')
@login_required(login_url='signin')
def home(request):
    return render(request,'home.html')

def log_out(request):
    logout(request)
    return redirect('/')

def edit(request):
    if request.user.is_authenticated:
        fm=Edituserform(instance=request.user)
        return render(request,'info.html',{'form':fm})
    else:
        return redirect('/')