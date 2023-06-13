"""
URL configuration for CrowdFunding project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myaccount.views import *
from django.conf.urls.static import static  # new
from django.conf import settings  # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/', include('projects.urls')),
    path('project/', include('projects.urls')),
    path('login', Login, name='Login'),
    path('Logout', Logout, name='Logout'),
    path('register', user_register, name='user_register'),
    path('userinfo/<int:id>', user_info, name='user_info'),
    # path('myview', my_view, name='my_view'),
    path('delete_account/<int:pk>', DeleteUser.as_view(), name='delete_account'),
    path('profileedit/<int:pk>', profile_edit.as_view(), name='profile_edit'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)  # new
