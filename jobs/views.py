from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Jobs, ApplyJob, Contact
from .forms import JobForm, ApplyJobForm, ContactForm
from django.views.generic import CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

    

class Add_Job(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = 'jobs/add_job.html'
   # fields = '__all__'

def job_detail(request, id):
    job_query = get_object_or_404(Jobs, id=id)
    context = {
        'q': job_query,
    }
    return render(request, "jobs/job_detail.html", context)

def jobs_view(request):
    query = Jobs.objects.all().count()

    qs = Jobs.objects.all().order_by('-published_date')
    paginator = Paginator(qs, 3)  # Show 3 jobs per page
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'query': qs,
        'job_qs': query

    }
    return render(request, 'jobs/jobs_view.html', context)

class Apply_Job(CreateView):
    model = ApplyJob
    form_class = ApplyJobForm
    template_name = 'jobs/job_apply.html'
    
 
def about_view(request):
    return render(request, 'jobs/about_us.html')

class Contact_Us(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'jobs/contact.html'

def our_services(request):
    return render(request, 'jobs/services.html')    

