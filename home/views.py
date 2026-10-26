from django.shortcuts import render

def landing(request):
    return render(request, 'home/landing.html')

def home(request):
    context = {
        'title': "Girlly's Home Page",
        'message': 'Welcome to my first Django application!',
        'show_message': True,
    }
    return render(request, 'home/home.html', context)
