from django.shortcuts import render
from django.http import HttpResponse

def reg(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def pulsar(request):
    return render(request,'pulsar.html')

def ktm(request):
    return render(request,'ktm.html')

def passion(request):
    return render(request,'passion.html')

def sucessfully_regr(request):
    return render(request,'sucessfully_regr.html')

def thankyou(request):
    return render(request,'thankyou.html')

def contact_us(request):
    return render(request,'contact_us.html')