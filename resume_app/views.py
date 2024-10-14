from django.shortcuts import render

# Create your views here.


def resume_creation(request):
    return render(request, "resume_app/resume_creation.html")
