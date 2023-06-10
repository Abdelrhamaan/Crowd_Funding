from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from .models import *




# Create your views here.


def user_register(request):

    context = {}
    if (request.method == 'POST'):
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        profile_pic=request.POST['pic']
        user = user_reg(first_name=first_name)
        user.last_name= last_name
        user.email = email
        user.profile_pic=profile_pic
        user.password = password
        user.save()
    return render(request, 'register.html', context)




def Login (request):
    return render(request,'login.html')
