from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def about_us(request):
    return render(request, 'about-us.html', {})


def activities(request):
    return render(request, 'activities.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def donate(request):
    return render(request, 'donate.html', {})

def projects(request):
    return render(request, 'projects.html', {}) 

def sponser(request):
    return render(request, 'sponser.html', {})

def sponsor_a_child(request):
    return render(request, 'sponsor-a-child.html', {})