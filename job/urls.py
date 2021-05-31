from django.urls import path , include

from .views import job_list , job_details

urlpatterns = [
    path('' ,job_list , name='all-jobs'),
    path('<int:id>' , job_details , name='job-details')
]
