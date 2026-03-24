from django.shortcuts import render, redirect
from .models import Influencer

def home(request):
    return render(request, 'home/index.html')


def get_started(request):
    return render(request, 'home/get_started.html')


def influencers(request):
    return render(request, 'home/influencers.html')



def join(request):
    if request.method == 'POST':
        Influencer.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            city=request.POST.get('city'),
            niche=request.POST.get('niche'),
            followers=request.POST.get('followers'),
            instagram=request.POST.get('instagram'),
            price=request.POST.get('price'),
            bio=request.POST.get('bio'),
        )
        return redirect('/influencer-dashboard/')
    
    return render(request, 'home/join.html')


def login(request):
    return render(request, 'home/login.html')


def profile(request):
    return render(request, 'home/profile.html')


def book(request):
    return render(request, 'home/book.html')


def dashboard(request):
    return render(request, 'home/dashboard.html')


def influencer_dashboard(request):
    return render(request, 'home/influencer_dashboard.html')