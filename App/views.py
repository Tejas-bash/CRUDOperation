from django.shortcuts import render,HttpResponseRedirect
from .forms import UserRegistration
from .models import User

# This will get the data from form
def add_show(request):
    if request.method == "POST":
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data.get('name')
            em = fm.cleaned_data.get('email')
            pw = fm.cleaned_data.get('password')
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            return HttpResponseRedirect('/')
    else:
        fm = UserRegistration()
    stud = User.objects.all()
    return render(request,'App/Addandshow.html',{'fm1':fm,'stu':stud})

# This Function will Update/Edit
def update_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        ft = UserRegistration(request.POST, instance=pi)
        if ft.is_valid():
            ft.save()
    else:
        pi = User.objects.get(pk=id)
        ft = UserRegistration(instance=pi)
    return render(request,'App/updatedata.html',{'fm1':ft})

# This Function will Delete
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    