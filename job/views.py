from django.shortcuts import render , HttpResponse

from .models import Jop

from django.views.generic import ListView , DetailView

# Create your views here.

# ****** function view Methodolgy ********
# def job_list(request):
    # job_list = Jop.objects.all()
    # context={
        # 'jobs':job_list
    # }

    # return render(request , 'job/job_list.html' ,context)
# 
# 
# def job_details(request,id):
    # job_details =Jop.objects.get(id=id)
    # print('='*20)
    # print(job_details)
    # context={
        # 'job':job_details
    # } 
    # return render(request , 'job/job_details.html' , context)
# 

# ****** Class Based view Methodolgy ********
class JobListView(ListView):
    model = Jop
    template_name='job/job_list.html'
    context_object_name='jobs'
    # paginate_by=2
    ordering=['-published_at']


class JobDetailsView(DetailView):
    model = Jop
    template_name = 'job/job_details.html'
    context_object_name = 'job'
