from django.shortcuts import redirect, render
from .models import Character
from acc.models import User
# Create your views here.

def index(request,bpk):
    c=User.objects.get(id=bpk)
    r=c.character_set.all()
    context={
        'cset':r,
    }
    return render(request,"character/index.html",context)

def detail(request,bpk):
    d=Character.objects.get(id=bpk)
    context={
        'd':d
    }
    return render(request,"character/detail.html",context)

def delete(request,bpk,rpk):
    re=Character.objects.get(id=rpk)
    re.delete()
    return redirect("character:index",bpk)

def create(request,bpk):
    if request.method=="POST":
        cn=request.POST.get("cname")
        cpic=request.FILES.get("cpic")
        cl=request.POST.get("clevel")
        cj=request.POST.get("cjob")
        Character(board=request.user,name=cn,level=cl,pic=cpic,job=cj).save()
        return redirect("character:index",bpk)
    return render(request,"character/create.html")

def update(request,bpk,rpk):
    d=Character.objects.get(id=rpk)
    if request.method=="POST":
        cn=request.POST.get("cname")
        cpic=request.FILES.get("cpic")
        cl=request.POST.get("clevel")
        cj=request.POST.get("cjob")
        if cpic:
            d.pic.delete()
            d.pic=cpic
        d.name,d.level,d.job=cn,cl,cj
        d.save()
        return redirect("character:index",bpk)
    context={
        'd':d
    }
    return render(request,"character/update.html",context)