from . import views
from django.urls import path

app_name = "resume_app"
urlpatterns = [
    path("creation", views.resume_creation, name="resume_creation")
]