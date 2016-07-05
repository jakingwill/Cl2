from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Job, Jobseeker, Employer
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    return render(request, "clockwork/index.html",{})

class AllJobsView(generic.ListView):
    template_name = 'clockwork/alljobsview.html'
    context_object_name = 'latest_job_list'

    def get_queryset(self):
        """Return the last five published jobs."""
        return Job.objects.order_by('date')[:100]



class IamajobseekerView(CreateView):
    model = Jobseeker
    fields = ['name', 'email', 'phone_number', 'home_location', 'industry', 'other_industry', 'id_number']
    #template_name = 'jobseekertemplate.html'


class PostajobView(CreateView):
    model = Job
    fields = ['employer', 'job_location', 'job_description', 'job_title', 'wage', 'date', 'time']

class IamanemployerView(CreateView):
    model = Employer
    fields = ['name', 'company', 'email', 'phone_no']
    #template_name = 'employertemplate.html'

class EmployerSeeMyJob(generic.DetailView):
    model = Job
    template_name = 'clockwork/employerseemyjob.html'

    def get_context_data(self, **kwargs):
        context=super(EmployerSeeMyJob, self).get_context_data(**kwargs)
        #job_pk = Job.objects.get(pk=self.kwargs.get('pk')) #Get this job's pk
        job_pk = self.kwargs['pk']
        context['jobseeker_list']=Job.objects.filter(pk=job_pk)[0].jobs.all()
        return context

class JobseekerJobView (generic.DetailView):
    model = Job
    template_name = 'clockwork/jobseekerjobview.html'

    

class JobseekerProfileView (generic.DetailView):
    model = Jobseeker
    template_name = 'clockwork/jobseekerprofileview.html'

class JobShortlistView(generic.ListView):
    template_name = 'clockwork/jobshortlistview.html'
    context_object_name = 'latest_job_shortlist'

    def get_queryset(self):
        """Return the last hundred published jobseekers."""
        return Jobseeker.objects.order_by('date')[:100]
    
class JobseekerApplied (generic.DetailView):
    model = Job
    template_name = 'clockwork/jobseekerapplied.html'

##def postjob(request, job_id):
##    return HttpResponse("Thanks for posting a job. Your job reference number is %s" % job_id)
##    job = get_object_or_404(Job, pk=pk)
##    try:
##        selected_employer = job.choice_set.get(pk=request.POST['employer'])
##    except (KeyError, Choice.DoesNotExist):
##        # Redisplay the question voting form.
##        return render(request, 'clockwork/detail.html',{'job': job,'error_message': "You didn't post a job.",})
##    
##    else:
##        selected_job.postjob += 1
##        selected_job.save()
##        # Always return an HttpResponseRedirect after successfully dealing
##        # with POST data. This prevents data from being posted twice if a
##        # user hits the Back button.
##        return HttpResponseRedirect(reverse('clockwork:postajob', args=(job.id)))
