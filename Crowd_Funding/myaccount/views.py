from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.


def user_register(request):
    return  render(request,'register.html')




def Login (request):
    return render(request,'login.html')
