from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def login(request):
     if request.method=='POST':
          username=request.POST.get('username','default')
          password=request.POST.get('password','default')

          user=auth.authenticate(username=username,password=password)

          if user is not None:
               auth.login(request,user)
               return redirect('/')
          else:
               messages.info(request,"invalid cridentials")
               return redirect('login')
          
     else:
          return render(request,'login.html')


def register(request):

    if request.method=='POST':
        first_name=request.POST.get('first_name','default')
        last_name=request.POST.get('last_name','default')
        username=request.POST.get('username','default')
        email=request.POST.get('email','default')
        password1=request.POST.get('password1','default')
        password2=request.POST.get('password2','default')  

        if password1==password2:
             if User.objects.filter(username=username).exists():
                  messages.info(request,'Username taken')
                  return redirect('register')

             elif User.objects.filter(email=email).exists():
                  messages.info(request,'email taken')
                  return redirect('register')
              
             else:
                  user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                  #we have created an object , now we will save it in the db
                  user.save();
                  print("user created")
                  return redirect('login')

        else:
            messages.info(request,'Passwords are not matching')
            return redirect('register')
    else:
        return render(request,'register.html')


def logout(request):
     auth.logout(request)
     return redirect('/')