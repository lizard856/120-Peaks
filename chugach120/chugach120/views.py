from django.shortcuts import render


def projects(request):
    return render(request, 'Projects.html')
