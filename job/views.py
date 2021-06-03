from job.forms import ApplyForm
from django.shortcuts import render , HttpResponse ,redirect

from .models import Category, Jop

from django.views.generic import ListView , DetailView

from django.contrib import messages

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
def job_details(request,slug):
    job_details =Jop.objects.get(slug=slug)
    if request.method == "POST":
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.jop = job_details
            myform.save()
            messages.success(request, f' Congratulations  {myform.name} Your Information Uploaded Succeffully!')
            # return redirect('job-details' )
         

    else :
        form = ApplyForm()

    context={
        'job':job_details,
        'form':form
    } 
    return render(request , 'job/job_details.html' , context)


# ****** Class Based view Methodolgy ********
class JobListView(ListView):
    model = Jop
    template_name='job/job_list.html'
    context_object_name='jobs'
    paginate_by=2
    ordering=['-published_at']
      


# class JobDetailsView(DetailView):
'''' i try to use DetailView gernaric to send form in context but h get error
 Method nor allowed and the bellow code when i send the form in post request
 i gess that becouse this generic dont support this methos but i don't sure about that
 so to less the headacke on my head i will use function based view that is good in this satiuation 
'''
    # model = Jop
    # template_name = 'job/job_details.html'
    # context_object_name = 'job'
    # # if request.method == "POST":
    # #     form = ApplyForm(request.POST , request.FILES)
    # #     if form.is_valid():
    # #         pass


    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     if self.request.method == "POST":
    #        form = ApplyForm(self.request.POST , self.request.FILES)
    #        if form.is_valid():
    #         myform = form.save()
    #         context['form']  = form

    #     else:
    #         form = ApplyForm()
    #         context['form'] = form
    #     return context







class CategoryListView(ListView):
    model = Category
    template_name='job/job_list.html'
    context_object_name='categories'
    # paginate_by=2
    ordering=['-id']
    