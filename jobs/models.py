from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

JOB_TYPE = (
    ('Part Time', 'Part Time'),
    ('Full Time', 'Full Time'),
    ('Freelance', 'Freelance'),
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Any', 'Any'),
)

class Jobs(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    company_name = models.CharField(max_length = 50)
    experience = models.CharField(max_length = 50)
    salary = models.CharField(max_length = 100, blank = True, null = True)
    description = models.TextField()
    job_location = models.CharField(max_length = 50)
    responsibilities = models.TextField()
    job_type = models.CharField(choices= JOB_TYPE, max_length = 50)
    gender = models.CharField(choices = GENDER, max_length = 50)
    total_vacancy = models.CharField(max_length = 10)
    application_deadline = models.DateTimeField()
    published_date = models.DateTimeField(default = timezone.now)
    image = models.ImageField(blank = True, null = True, upload_to = 'media')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

class ApplyJob(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    CV = models.FileField(null=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.first_name