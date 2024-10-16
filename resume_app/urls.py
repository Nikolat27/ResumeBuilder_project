from . import views
from django.urls import path

app_name = "resume_app"
urlpatterns = [
    path("creation", views.ResumeCreationView.as_view(), name="resume_creation"),
    path("all", views.all_resumes, name="all_resumes"),
    path("detail/<int:pk>", views.retrieve_resume, name="retrieve_resume"),
]
