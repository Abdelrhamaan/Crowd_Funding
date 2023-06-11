from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
import re

from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
from django.contrib.auth import login, authenticate


# Create your views here.


def user_register(request):
    context = {}
    if (request.method == 'POST'):
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_pass']
        profile_pic = request.FILES['pic']
        if (password == confirm_password):
            user = user_reg(first_name=first_name)
            user.last_name = last_name
            user.email = email
            user.profile_pic = profile_pic
            user.password = password
            user.save()
        else:
            context['notmatch'] = 'the password is not matched '
    return render(request, 'register.html', context)


# def my_view(request):
#     if request.method == 'POST':
#         form = MyModelForm(request.POST, request.FILES)
#         print(form)
#         if form.is_valid():
#             form.save()
#             return redirect('my_view')
#     else:
#         form = MyModelForm()
#     return render(request, 'image.html', {'form': form})
#


def Login(req):
    context = {}
    if (req.method == 'POST'):
        info_valid = user_reg.objects.filter(email=req.POST['email'], password=req.POST['password'])
        if (len(info_valid) != 0):
            req.session['firstname'] = info_valid[0].first_name
            get_user_id = info_valid[0].id
            return HttpResponseRedirect(f'userinfo/{get_user_id}')
        else:
            context['invalid'] = 'the email address is not exist plz enter valid email '

    return render(req, 'login.html', context=context)


def user_info(request, id):
    if ('firstname' in request.session):
        context = {}
        context['logged_in_user'] = user_reg.objects.filter(id=id)
        print(context)
        return render(request, 'user_info.html', context)
    else:
        return HttpResponseRedirect('login')



# class profile_edit(generic.UpdateView ):
#     model = user_reg
#     template_name = 'user_edit.html'
#
#
#     fields = [  'first_name',
#               'last_name',
#               'phone_num',
#               'profile_pic',
#               'birth_date',
#               'fb_profile']

class profile_edit(generic.UpdateView):
    model = user_reg
    template_name = 'user_edit.html'
    form_class = profile_edit_form
    success_url = '/'

    def get_success_url(self):
        return reverse_lazy('user_info', kwargs={'id': self.object.id})
    # def get_success_url(self):
    #     id = self.kwargs['id']
    #     return reverse_lazy('user_info', kwargs={'id': id})

# def adminregister(req):
#     myForm = user_reg()
#     context = {}
#     context['form'] = myForm
#     if (req.method=='POST'):
#         myForm = user_reg(req.POST)
#         if(myForm.is_bound and myForm.is_valid()):
#             User.objects.create_superuser(username=req.POST ['username'],email=req.POST['email'],password=req.POST['password'])
#             return HttpResponseRedirect('/admin')
#     return render(req, 'adminregister.html' , context)
