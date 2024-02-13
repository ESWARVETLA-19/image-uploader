from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import Image
from .forms import CreateUSerForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'home.html',{'form':form,'img':Image.objects.all()})
    else:
        form = ImageForm()
    return render(request,'home.html',{'form':form,'img':Image.objects.all()})

def register(request):
    form= CreateUSerForm()
    if request.method=="POST":
        form=CreateUSerForm(request.POST)
        if form.is_valid():
            user=form.save()
            Username=form.cleaned_data.get('username')
            messages.success(request,"profile was created for"+ Username)
            return render(request,'login.html')
    context={'form':form}
    return render(request,'register.html',context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Username or password may be incorrect")
    context = {}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')


