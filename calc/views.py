from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    params1={'name':'Devaa'}
    return render(request,'home.html',params1)

def add(request):
    val1=request.POST.get('num1','default')
    val2=request.POST.get('num2','default')
    sure=request.POST.get('sure','off')

    if sure=="on" :
        res=int(val1) + int(val2)
    else:
        return HttpResponse("Error")
    params2={'result':res}
    return render(request,'result.html',params2)