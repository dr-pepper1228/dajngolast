from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from .models import User

# Create your views here.

def index(request):
    return render(request,"acc/index.html")

def login_user(request):
    if request.method=="POST":
        un=request.POST.get("uname")
        up=request.POST.get("upass")
        user=authenticate(username=un,password=up)
        if user:
            login(request,user)
            return redirect("acc:index")
        else:
            pass 
    return render(request,"acc/login.html")

def logout_user(request):
    logout(request)
    return redirect("acc:index")

def profile(request):
    return render(request,"acc/profile.html")

def delete(request):
    if request.user.pic:
        request.user.pic.delete()
    request.user.delete()
    return redirect("acc:index")

def signup(request):
    if request.method=="POST":
        un=request.POST.get("uname")
        up=request.POST.get("upass")
        try:
            User.objects.create_user(username=un,password=up)
            user=authenticate(username=un,password=up)
            login(request,user)
            return redirect("acc:index")
        except:
            pass
    return render(request,"acc/signup.html")

def update(request):
    u=request.user
    if request.method=="POST":
        up=request.POST.get("upass")
        upic=request.FILES.get("upic")
        um=request.POST.get("umail")
        uc=request.POST.get("ucomm")
        if up:
            u.set_password(up)
        if upic:
            u.pic.delete()
            u.pic=upic
        u.email=um 
        u.comment=uc 
        u.save()
        return redirect("acc:profile")
    return render(request,"acc/update.html")