from django.shortcuts import render , HttpResponse

# Create your views here.



def job_list(request):
    return HttpResponse('<h1> Job List  </h1>')

def job_details(request,id):
    return HttpResponse(f'<h1> Job num [{id}]</h1>')