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
        return render(request, 'project/create_project.html', {'categories': categories, 'tags': tags})
    
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
    images=Photo.objects.filter(project=project)
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
    context['remainingAmout']=project.target - totaldonation
    context['donateRatio']=totaldonation/project.target *100
    
    rates= Rate.objects.filter(project=ID)
    totalrate=0
    for rate in rates:
        totalrate=totalrate+rate.rate
    if len(rates)>0:
        totalrate=totalrate/(len(rates))
    context['totalrate']=totalrate
    context['rateRatio']=totalrate/5*100
    
    tags=project.tags.filter(project=ID)
    context['tags']=tags
    
    
    reports = Report.objects.filter(project=ID)
    context['reports'] = reports
    
    
    
    projects_similar=get_similar_projects(ID)
    images_similar={}
    for project in projects_similar:
        images_similar[project]=Photo.objects.filter(project=project)
    # print(images[project][0].image.url)
        
    
    context['projects_similar']=projects_similar
    context['images_similar']=images_similar
    
    return  render(request,'project/project_page.html',context)
    

def addComment(request,ID):

    if request.method == 'POST':
        comment = request.POST['comment']
        project = Project.objects.get(id=ID)
        user=user_reg.objects.get(id="4")
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
        amount = int(request.POST['amount'])
        project = Project.objects.get(id=ID)
        user=user_reg.objects.get(id="4")
        # user = request.session['username']
        # user = user_reg.objects.get(username=user)
        donations= Donation.objects.filter(project=ID)
        totaldonation=0
        for  donation in donations:
            totaldonation=totaldonation+donation.amount
        if (amount<=(project.target-totaldonation)):
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
        user=user_reg.objects.get(id="4")
        # user = request.session['username']
        # user = user_reg.objects.get(username=user)
        preRates=Rate.objects.filter(project=project)
        cond =True
        for rate in preRates:
            if rate.user ==user:
                cond=False 
        if cond:
            Rate.objects.create(
                project=project,
                user=user,
                rate=int (rate)
            )
        return redirect('projectView', ID=ID)
    else:
        return redirect('projectView', ID=ID)
    
    
def addReport(request,ID):
    if request.method == 'POST':
    
        project = Project.objects.get(id=ID)
        user=user_reg.objects.get(id="4")
        # user = request.session['username']
        # user = user_reg.objects.get(username=user)
        preReports=Report.objects.filter(project=project)
        cond =True
        for report in preReports:
            if report.user ==user:
                cond=False 
        if cond:
            Report.objects.create(
                project=project,
                user=user,
                report=True,
            )
        return redirect('projectView', ID=ID)
    else:
        return redirect('projectView', ID=ID)


def get_similar_projects(id):
    project = Project.objects.get(id=id)
    tags = project.tags.filter(project=id)
    similar_projects = []
    for tag in tags:
        similar_projects += tag.project_set.all()
    similar_projects = list(set(similar_projects))
    similar_projects.remove(project)
    print(similar_projects)
    return similar_projects
