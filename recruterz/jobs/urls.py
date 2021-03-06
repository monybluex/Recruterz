from django.urls import path
from . import views

urlpatterns = [
    path('jobs', views.jobs, name='jobs'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('postjobs', views.postjobs, name='postjobs'),
    path('details', views.details, name='details')
]
