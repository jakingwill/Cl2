from django.contrib import admin

from .models import Job

admin.site.register(Job)

from .models import Employer

admin.site.register(Employer)

from .models import Jobseeker

admin.site.register(Jobseeker)
