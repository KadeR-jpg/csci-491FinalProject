from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.storyGen, name='landingPage'),
    path('about/', views.about, name='about'),
    path('generate/', views.storyGen, name='storyGen'),
    path('nextStory/', views.next, name='next'),
    path('prevStory/', views.prev, name='prev')
]
