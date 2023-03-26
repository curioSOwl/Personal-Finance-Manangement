from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import Details
from django.contrib.auth import authenticate,login
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
import calendar
import datetime
from .models import Transactions
from .forms import TransactionForm

from datetime import *
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request,'index.html')

def dashb(request):
    
    
    items=Transactions.objects.filter(user=request.user).order_by('date')
   
    context={
        'items':items,
    }

    return render(request,'dashb.html',context)


def trans(request):
    items=Transactions.objects.filter(user=request.user)
    trans_tod=Transactions.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            try: 
                detaileq=Details.objects.get(username=request.user)
            except Details.DoesNotExist:
                return HttpResponse('NO PROFILE FOUND')
            print("hello")
            print(detaileq.curbal,instance.price,instance.date)
            
            if detaileq.curbal-instance.price>0:
                print(date.today())
                for i in trans_tod:
                    if instance.date==datetime.today():
                        detaileq.Today_ex+=instance.price
                instance.save()
                detaileq.curbal-=instance.price
                detaileq.save()
            else:

                HttpResponse("Insufficient balance")
            
            print("yess")
            return redirect('trans')
        else:
            print("form invalid")
    
    else:
        form = TransactionForm()

    context={
        'items':items,
        'form':form,
    }
    return render(request,'trans.html',context)

def stat(request):
    data = Transactions.objects.filter(user=request.user)

    context={
        'data': data,
    }
    return render(request,'statistics.html',context)

def sett(request):
    return render(request,'settings.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('signin')
    return render(request,'signup.html')



def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        print(request.POST)
        if user is not None:
            login(request,user)
            return redirect('dash')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'signin.html')



def profile_update(request):
    if request.method=='POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.details)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('sett')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.details)
    
    context = {
        'user_form': user_form,
        'profile_form':profile_form,
    }
    return render(request,'profile_update.html', context)
