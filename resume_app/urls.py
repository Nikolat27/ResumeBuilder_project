from . import views
from django.urls import path

app_name = "resume_app"
urlpatterns = [
    path("creation", views.ResumeCreationView.as_view(), name="resume_creation")
]
