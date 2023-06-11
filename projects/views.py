from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone

from .models import *
def projectList(request):
    # if( 'username' in request.session):
    projects=Project.objects.all()
    images={}
    for project in projects:
        images[project]=Photo.objects.filter(project=project)
    # print(images[project][0].image.url)
        
    context={}
    context['projects']=projects
    context['images']=images
    
    return  render(request,'project/list.html',context)#HttpResponse('hi from project list view')
    # else:
    #     return HttpResponseRedirect('/')
    
    
    
    
    
    
    

def projectAdd(request):
    if request.method == 'POST':
        title = request.POST['title']
        details = request.POST['details']
        category_id = request.POST['category']
        category = Category.objects.get(id=category_id)
        target = request.POST['target']
        tag_ids = request.POST.getlist('tags')
        tags = Tag.objects.filter(id__in=tag_ids)
        pub_date = timezone.now()
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        project = Project.objects.create(
            title=title,
            details=details,
            category=category,
            target=target,
            pub_date=pub_date,
            start_date=start_date,
            end_date=end_date
        )
        images = request.FILES.getlist('images')
        for imag in images:
        
            photo = Photo.objects.create(
                project=project,
                image=imag,

            )
        project.tags.set(tags)
        return redirect("projectlist")
    else:
        categories = Category.objects.all()
        tags = Tag.objects.all()
        return render(request, 'project/add.html', {'categories': categories, 'tags': tags})
    
def projectDelete(request,ID):
    project=Project.objects.get(id=ID)
    project.delete()
    return redirect('projectlist')


def userProject(request):
    # if( 'username' in request.session):
    projects=Project.objects.all()
    images={}
    for project in projects:
        images[project]=Photo.objects.filter(project=project)
    # print(images[project][0].image.url)
        
    context={}
    context['projects']=projects
    context['images']=images
    
    return  render(request,'project/userproject.html',context)


def projectView(request,ID):
    # if( 'username' in request.session):
    project=Project.objects.get(id=ID)
    images=Photo.objects.filter(project=ID)
    context={}
    context['project']=project
    context['images']=images
    comments = Comment.objects.filter(project=ID)
    context['comments'] = comments
    
    donations= Donation.objects.filter(project=ID)
    totaldonation=0
    for  donation in donations:
        totaldonation=totaldonation+donation.amount
    context['totaldonation']=totaldonation
    
    rates= Rate.objects.filter(project=ID)
    totalrate=0
    for rate in rates:
        totalrate=totalrate+rate.rate
    if len(rates)>0:
        totalrate=totalrate/(len(rates)*5)
    context['totalrate']=totalrate
    
    tags=project.tags.filter(project=ID)
    context['tags']=tags
    return  render(request,'project/viewproject.html',context)
    

def addComment(request,ID):

    if request.method == 'POST':
        comment = request.POST['comment']
        project = Project.objects.get(id=ID)
        user=user_reg.objects.get(id="1")
        # user = request.session['username']
        # user = user_reg.objects.get(username=user)
        Comment.objects.create(
            project=project,
            user=user,
            comment=comment
        )
        return redirect('projectView', ID=ID)
    else:
        return redirect('projectView', ID=ID)
    
def addDonation(request,ID):
    if request.method == 'POST':
        amount = request.POST['amount']
        project = Project.objects.get(id=ID)
        user=user_reg.objects.get(id="1")
        # user = request.session['username']
        # user = user_reg.objects.get(username=user)
        Donation.objects.create(
            project=project,
            user=user,
            amount=amount
        )
        return redirect('projectView', ID=ID)
    else:
        return redirect('projectView', ID=ID)


def addRate(request,ID):
    if request.method == 'POST':
    
        rate = request.POST['rate']
        project = Project.objects.get(id=ID)
        user=user_reg.objects.get(id="1")
        # user = request.session['username']
        # user = user_reg.objects.get(username=user)
        Rate.objects.create(
            project=project,
            user=user,
            rate=int (rate)
        )
        return redirect('projectView', ID=ID)
    else:
        return redirect('projectView', ID=ID)
