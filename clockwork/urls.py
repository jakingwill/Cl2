from django.conf.urls import url

from . import views

app_name = 'clockwork'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^alljobsview/', views.AllJobsView.as_view(), name='alljobsview'),
    url(r'^jobshortlistview/', views.JobShortlistView.as_view(), name='jobshortlistview'),
    url(r'^iamajobseeker/', views.IamajobseekerView.as_view(), name='iamajobseeker'),
    url(r'^postajob/', views.PostajobView.as_view(), name='postajob'),
    url(r'^iamanemployer/', views.IamanemployerView.as_view(), name='iamanemployer'),
    #url(r'^employerseemyjob/', views.EmployerSeeMyJob.as_view(), name='employerseemyjob'),
    url(r'^(?P<pk>[0-9]+)/employerseemyjob/$', views.EmployerSeeMyJob.as_view(), name='employerseemyjob'),
    url(r'^(?P<pk>[0-9]+)/jobseekerjobview/$', views.JobseekerJobView.as_view(), name='jobseekerjobview'),
    url(r'^(?P<pk>[0-9]+)/jobseekerprofileview/$', views.JobseekerProfileView.as_view(), name='jobseekerprofileview'),
    url(r'^(?P<pk>[0-9]+)/jobseekerapplied/$', views.JobseekerApplied.as_view(), name='jobseekerapplied'),
]
