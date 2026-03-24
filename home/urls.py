from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),


    path('get-started/', views.get_started, name='get_started'),


     path('influencers/', views.influencers, name='influencers'),


     path('join/', views.join, name='join'),


     path('login/', views.login, name='login'),


     path('profile/', views.profile, name='profile'),


     path('book/', views.book, name='book'),


     path('dashboard/', views.dashboard, name='dashboard'),

     path('influencer-dashboard/', views.influencer_dashboard, name='influencer_dashboard'),
]