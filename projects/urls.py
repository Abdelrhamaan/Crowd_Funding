from django.urls import path
from .views import *

urlpatterns = [
    path('',projectList,name='projectlist'),
    path('add',projectAdd,name='projectadd'),
    # path('Add',projectAdd,name='projectadd'),
    path('Update/<int:ID>',projectUpdate,name='projectupdate'),
    path('Delete/<int:ID>',projectDelete,name='projectDelete'),
    path("UserProject",UserProject,name="UserProject"),
    
]