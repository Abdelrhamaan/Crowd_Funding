from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import *
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
import re
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.utils.timezone import now
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.urls import reverse_lazy, reverse


# def user_register(request):
#     if request.method == 'POST':
#         form = user_reg(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.activation_key = get_random_string(length=40)
#             user.save()

#             # Send activation email
#             subject = 'Activate your account'
#             message = f'Hi {user.username},\n\nPlease click the following link to activate your account:\n\nhttp://localhost:8000/activate/{user.activation_key}/\n\nThis link will expire in 24 hours.\n\nThanks!'
#             from_email = 'noreply@example.com'
#             recipient_list = [user.email]
#             send_mail(subject, message, from_email, recipient_list)

#             return render(request, 'registration/register_done.html', {'user': user})
#     else:
#         form = UserRegisterForm()
#     return render(request, 'registration/register.html', {'form': form})
# Create your views here.


# def user_register(request):

#     context = {}
#     if request.method == 'POST':
#         # print(request.POST)
#         # define form content
#         first_name = request.POST['firstname']
#         last_name = request.POST['lastname']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_pass']
#         profile_pic = request.FILES['pic']
#         egy_phone_number = request.POST["egy_phone_number"]
#         phone_regex = r'^01[0125][0-9]{8}$'
#         if re.match(phone_regex, egy_phone_number):
#             if password == confirm_password:
#                 # Define a Django model for the user_reg object
#                 user = user_reg(first_name=first_name)
#                 user.last_name = last_name
#                 user.email = email
#                 user.profile_pic = profile_pic
#                 user.password = password
#                 user.egy_phone_number = egy_phone_number
#                 # check if form is valid to send activation key
#                 form = user_reg(request.POST)
#                 if form.is_valid():
#                     user = form.save()
#                     user.is_active = False
#                     user.activation_key = get_random_string(length=40)
#                     user.save()
#                     # Send activation email
#                     subject = 'Activate your account'
#                     message = f'Hi {user.username},\n\nPlease click the following link to activate your account:\n\nhttp://localhost:8000/activate/{user.activation_key}/\n\nThis link will expire in 24 hours.\n\nThanks!'
#                     from_email = 'noreply@example.com'
#                     recipient_list = [user.email]
#                     send_mail(subject, message, from_email,
#                               recipient_list, fail_silently=False)
#                     return render(request, 'login.html', {'user': user})
#             else:
#                 context['notmatch'] = 'The password and confirm password fields do not match.'
#         else:
#             context['notmatch'] = 'The Phone Number should be 11 and Egyptian number.'

#     return render(request, 'register.html', context)

def user_register(request):
    context = {}
    if ('email' in request.session):
        email = request.session['email']
        logged_user_id = user_reg.objects.get(email=email).id
        return redirect(f'userinfo/{logged_user_id}')
    else:
        if request.method == 'POST':
            print(request.POST)
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm_pass']
            profile_pic = request.FILES['pic']
            egy_phone_number = request.POST["egy_phone_number"]
            phone_regex = r'^01[0125][0-9]{8}$'

            if re.match(phone_regex, egy_phone_number):
                if password == confirm_password:
                    # Define a Django model for the user_reg object
                    user = user_reg(first_name=first_name)
                    user.last_name = last_name
                    user.email = email
                    user.profile_pic = profile_pic
                    user.password = password
                    user.egy_phone_number = egy_phone_number
                    user.save()

                else:
                    context['notmatch'] = 'The password and confirm password fields do not match.'
            else:
                context['notmatch'] = 'The Phone Number should be 11 and Egyptian number.'

        return render(request, 'register.html', context)


class DeleteUser(SuccessMessageMixin, generic.DeleteView):
    model = user_reg
    template_name = 'delete_account_confirmation.html'
    # ???
    success_message = "user has been deleted"
    success_url = reverse_lazy('Login')

    # pk_url_kwarg = 'id'
    # def delete_session(self):

    def get_context_data(self, **kwargs):
        self.request.session.clear()
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class profile_edit(generic.UpdateView):
    model = user_reg
    template_name = 'user_edit.html'
    form_class = profile_edit_form
    success_url = '/'

    def get_success_url(self):
        return reverse_lazy('user_info', kwargs={'id': self.object.id})


def Login(req):
    context = {}
    if ('email' in req.session):
        email = req.session['email']
        logged_user_id = user_reg.objects.get(email=email).id
        return redirect(f'userinfo/{logged_user_id}')
    else:
        if (req.method == 'POST'):
            info_valid = user_reg.objects.filter(
                email=req.POST['email'], password=req.POST['password'])
            if (len(info_valid) != 0):
                req.session['email'] = info_valid[0].email
                # print(req.session, "session")
                get_user_id = info_valid[0].id
                # print(get_user_id)
                return HttpResponseRedirect(f'userinfo/{get_user_id}')
            else:
                context['invalid'] = 'the email address is not exist plz enter valid email '

        return render(req, 'login.html', context=context)


def Logout(req):
    req.session.clear()
    return HttpResponseRedirect('login')


def user_info(request, id):
    # print(id)
    if ('email' in request.session):
        email = request.session['email']
        logged_user_id = user_reg.objects.get(email=email).id
        # print(logged_user_id)
        # print(email)
        if (logged_user_id == id):
            context = {}
            context['logged_in_user'] = user_reg.objects.filter(id=id)
            # print(context)
            return render(request, 'user_info.html', context)
        else:
            return HttpResponse('NOT Found')
    else:
        return redirect('/login')
