from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from .forms import SignUpForm
from modelexpense.models import Category
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect


# Create your views here.
def home(request):
    records = Category.objects.all()
    if request.method=='POST':
         username=request.POST['username']
         password=request.POST['password']
         user=authenticate(request,username=username,password=password)
         if user is not None:
                        login(request,user)
                        messages.success(request,"You Have Been Logged")
                        return redirect('home')
         else:
                        messages.success(request,"Something Went Wrong. Error...")
    
    return render(request,'home.html',{'records':records})
def aboutus(request):
    return render(request,'about.html',{})

def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')
def login_user(request):
       pass
def register_user(request):
        
                 form=SignUpForm(request.POST )
                 if form.is_valid():
                         form.save()
                         #Aunthenticate and login
                         username = form.cleaned_data['username']
                         password = form.cleaned_data['password1']
                         user = authenticate(username=username, password=password)
                         login(request, user)
                         messages.success(request, "You Have Successfully Registered! Welcome!")
                         return redirect('home')
                 return render(request,"register_user.html",{'form':form})
#return render(request,"register_user.html",{'form':form})
