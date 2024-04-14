from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_greetings, name="home"),
    path('about_me/', views.about_me, name="about_me"),
    path('contact/',views.contact,name='contact'),
    path('projects/',views.projects,name='projects'),    
]
