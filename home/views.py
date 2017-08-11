from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def comingsoon(request):
    return render(request, 'home/coming-soon.html')


