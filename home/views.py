from django.shortcuts import render

# imort projects models
from projects.models import Project
from myaccount.models import user_reg
from projects.models import Photo

from django.http import HttpResponse

# imort projects models




# Create your views here.




def home(request):
    context = {}
    images = {}
 

    projects_rated = Project.objects.all().order_by('-average_rate')[:4]
    context['projects_rated'] = projects_rated

    print(context['projects_rated'])

    for project in projects_rated:
        project_id = project.id
        images[project] = Photo.objects.filter(project=project_id)
      

 
    projects_recent = Project.objects.all().order_by('-pub_date')[:4]
    context['projects_recent'] = projects_recent


    if ('email' in request.session):
        email = request.session['email']
        profile_pic = user_reg.objects.get(email=email).profile_pic

        context['profile_pic'] = profile_pic
   



    return  render(request,'index.html', context)#HttpResponse('hi from project list view')


# def user_profile_pic(request):
#     context = {}
#     if ('email' in request.session):
#         email = request.session['email']
#         user = user_reg.objects.get(email=email)
#         context['user'] = user
#         print(context)
#         return render(request, 'index.html', context)
#     else:
#         return HttpResponse('NOT Found')


def top_four_rated(request):
    slider = {}
    projects_rated = Project.objects.all().order_by('-average_rate')[:4]
    slider['projects_rated'] = projects_rated

    print(slider['projects_rated'])

    projects = Project.objects.all()
    images = {}
    for project in projects:
        images[project] = Photo.objects.filter(project=project)
    slider['images'] = images
    print(slider['images'])

    return  render(request,'index.html', slider)#HttpResponse('hi from project list view')




