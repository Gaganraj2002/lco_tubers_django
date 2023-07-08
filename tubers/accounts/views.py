from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are logged in')
            return redirect("dashboard")
        else:
            messages.warning(request,"Invalid Credentials")
            return redirect("login")
    return render(request,"accounts/login.html")

def register(request):
    if request.method=="POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request,"Username already exists")
                return redirect("register")
                print("Username already exists")
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request,"Email already Registered")
                    return redirect("register")
                    print("Email already exists")
                else:
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                    user.save()
                    messages.success(request,"Account Created Succesfully")
                    print("Saved")
                    return redirect('login')
        else:
            messages.warning(request,"Passwords Doesnt Match")
            print("Password Doesnt match")
            return redirect("register")
    return render(request,"accounts/register.html")

def logoutUser(request):
    logout(request)
    return redirect("Home")

@login_required(login_url='login')
def dashboard(request):
    return render(request,"accounts/dashboard.html")
