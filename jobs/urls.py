from django.urls import path
from jobs.views import jobs_view, about_view, Contact_Us, our_services, Add_Job, job_detail, Apply_Job

app_name = 'jobs'

urlpatterns = [ 

    path('add_job/', Add_Job.as_view(), name = 'add-job'),
    path('jobs_view/', jobs_view, name = 'job-view'),
    path('about_us/', about_view, name = 'about-view'),
    path('contact_us/', Contact_Us.as_view(), name = 'contact-us'),
    path('job_detail/<int:id>/', job_detail, name='job-detail'),
    path('services/', our_services, name = 'our-services'),
    path('apply/', Apply_Job.as_view(), name='apply'),
]


