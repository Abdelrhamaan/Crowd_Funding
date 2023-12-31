from django.urls import path
from .views import *

urlpatterns = [
    path('',projectList,name='projectlist'),
    path('add',projectAdd,name='projectadd'),
    # path('Add',projectAdd,name='projectadd'),
    # path('Update/<int:ID>',projectUpdate,name='projectupdate'),
    # path('Delete/<int:ID>',projectDelete,name='projectDelete'),
    path('Delete/<int:ID>',projectDelete,name='projectDelete'),
    path("UserProject",userProject,name="userProject"),
    path("view/<int:ID>",projectView,name="projectView"),
    path("donate/<int:ID>",addDonation,name="addDonation"),
    path("comment/<int:ID>",addComment,name="addComment"),
    path("rate/<int:ID>",addRate,name="addRate"),
    path("report/<int:ID>",addReport,name="addreport"),
]