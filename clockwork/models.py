from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.core.urlresolvers import reverse

INDUSTRY_CHOICES = (
    ('Construction','Construction'),
    ('Promotions','Promotions'),
    ('Events', 'Events'),
    ('Barwork', 'Barwork'),
    ('Gardener', 'Gardening'),
    ('Cleaning', 'Cleaning'),
    ('Transport', 'Transport'),
    )

class Employer(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_no = models.CharField(max_length=12)

    def __str__(self):
        return self.name

class Jobseeker (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=12) 
    home_location = models.CharField(max_length=150)
    industry = models.CharField(max_length=12, choices=INDUSTRY_CHOICES)
    other_industry = models.CharField(max_length=150)
    id_number = models.CharField(primary_key=True, max_length=13)
    

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('clockwork:jobseekerprofileview', kwargs={'pk':self.pk})


class Job(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    time = models.TimeField(default=datetime.now)
    job_location = models.CharField(max_length=150)
    job_description = models.CharField(max_length=180)
    job_title = models.CharField(max_length=20)
    wage = models.CharField(max_length=6, default=0)
    jobs = models.ManyToManyField(Jobseeker)

    def __str__(self):              # __unicode__ on Python 2
        return self.job_title
        self.employer_id

    def get_absolute_url(self):
        return reverse('clockwork:employerseemyjob', kwargs={'pk':self.pk})


##class Shortlist (models.Model):
##
##    jobseeker_id = models.ForeignKey(Jobseeker, on_delete=models.CASCADE) #reference jobseeker model
##    job_id = models.ForeignKey(job_id, on_delete=models.CASCADE) #reference job model
    
