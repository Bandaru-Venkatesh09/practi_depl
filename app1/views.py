from django.shortcuts import render,redirect

from app1.models import hostel
from app1.form import hostel_form
from app1.form1 import hostel_form1

def details(request):
    data=hostel.objects.all()
    context={
        'data':data
    }
    return render(request,'frant/home.html',context)

def new_hostel_form(request):
    form=hostel_form()
    if request.method=='POST':
        form=hostel_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=hostel_form()
    context={
        'form':form
        }
    return render(request,'frant/form.html',context)

def update(request,id):
    data=hostel.objects.get(id=id)
    if request.method=='POST':
        form=hostel_form1(request.POST,instance=data)
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form=hostel_form1(instance=data)
    context={
        'form':form
    }
    return render(request,'frant/form1.html',context)

def delete(request,id):
    data=hostel.objects.get(id=id)
    data.delete()
    return redirect('home')
    