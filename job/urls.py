from django.urls import path , include

from .views import(
    #  job_list , 
     job_details,
     JobListView,
    #  JobDetailsView
     
)

urlpatterns = [
    path('' ,JobListView.as_view() , name='all-jobs'),
    path('<str:slug>' , job_details , name='job-details') #note if you will user DetailView generic you must use pk or slug not id...Ok
    
]
