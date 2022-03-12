from django.shortcuts import redirect, render
from .models import Job,Reply
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    kw=request.GET.get("kw","")
    cate=request.GET.get("cate","")
    if kw:
        if cate=="ro":
            d=Job.objects.filter(root__contains=kw)
        elif cate=="name":
            d=Job.objects.filter(name__contains=kw)
    else:
        d=Job.objects.all()
    page=request.GET.get("page",1)
    pag=Paginator(d,5)
    obj=pag.get_page(page)
    context={
        'dset':obj,
        "cate": cate,
        "kw": kw
    }
    return render(request,"lclass/index.html",context)

def detail(request,bpk):
    d=Job.objects.get(id=bpk)
    r=d.reply_set.all()
    context={
        'd':d,
        'rset':r
    }
    return render(request,"lclass/detail.html",context)

def creply(request,bpk):
    b=Job.objects.get(id=bpk)
    if request.method=="POST":
        rc=request.POST.get("comm")
        Reply(board=b,replyer=request.user,comment=rc).save()
    return redirect("lclass:detail",bpk)

def dreply(request,bpk,rpk):
    re=Reply.objects.get(id=rpk)
    if request.user == re.replyer:
        re.delete()
    return redirect("lclass:detail",bpk)

def likey(request,bpk):
    b=Job.objects.get(id=bpk)
    b.likey.add(request.user)
    return redirect("lclass:detail",bpk)

def cancel(request,bpk):
    b=Job.objects.get(id=bpk)
    b.likey.remove(request.user)
    return redirect("lclass:detail",bpk)