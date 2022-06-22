from django import forms
from .models import Jobs, ApplyJob, Contact
from django.utils import timezone


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

class JobForm(forms.ModelForm):

    class Meta:
        model = Jobs
        fields = ('username','title', 'company_name', 'job_location', 'experience', 'salary',
        'description','job_type', 'gender', 'total_vacancy', 'responsibilities', 'application_deadline',
        'image')

        widgets = {

            'username' : forms.Select(attrs = {'class': 'form-control'}),
            'title' : forms.TextInput(attrs = {'class': 'form-control'}),
            'company_name' : forms.TextInput(attrs = {'class': 'form-control'}),
            'job_location' : forms.TextInput(attrs = {'class': 'form-control'}),
            'experience' : forms.TextInput(attrs = {'class': 'form-control'}),
            'salary' : forms.TextInput(attrs = {'class': 'form-control'}),
            'description' : forms.Textarea(attrs = {'class': 'form-control'}),
            'job_type' : forms.Select(choices= JOB_TYPE,attrs = {'class': 'form-control'}),
            'gender' : forms.Select(choices= GENDER,attrs = {'class': 'form-control'}),
            'total_vacancy' : forms.TextInput(attrs = {'class': 'form-control'}),
            'responsibilities' : forms.TextInput(attrs = {'class': 'form-control'}),
            'application_deadline' : forms.DateTimeInput(attrs = {'placeholder': '2020-12-27'}),
           # 'image' : forms.ImageInput(),

        }
class ApplyJobForm(forms.ModelForm):

    class Meta:
        model = ApplyJob
        fields = '__all__'
        
        widgets = {

            'name' : forms.TextInput(attrs = {'class': 'form-control'}),
            'email' : forms.EmailInput(attrs = {'class': 'form-control'}),
            'CV' : forms.FileInput(attrs = {'class': 'form-control'}),
        }

        labels = {
            "CV": "CV (pdf format)",
            "name": "Full Name"
        }

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
        
        widgets = {

            'first_name' : forms.TextInput(attrs = {'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs = {'class': 'form-control'}),
            'Email' : forms.EmailInput(attrs = {'class': 'form-control'}),
            'subject' : forms.TextInput(attrs = {'class': 'form-control'}),
            'message' : forms.Textarea(attrs = {'class': 'form-control'}),
        }