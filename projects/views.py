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
        print("*****************************************************************8")
        print(images)
        print("*****************************************************************8")
        for image in images:
            print(image)
            photo = Photo.objects.create(
                project=project,
                image=image,

            )
        project.tags.set(tags)
        return redirect("projectlist")
    else:
        categories = Category.objects.all()
        tags = Tag.objects.all()
        return render(request, 'project/add.html', {'categories': categories, 'tags': tags})