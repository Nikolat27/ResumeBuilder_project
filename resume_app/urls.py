from . import views
from django.urls import path

app_name = "resume_app"
urlpatterns = [
    path("creation", views.ResumeCreationView.as_view(), name="resume_creation"),
    path("all", views.all_resumes, name="all_resumes"),
    path("detail/<int:pk>", views.retrieve_resume, name="retrieve_resume"),
    path('update/<int:pk>/', views.resume_update, name='resume_update'),
    path('delete/<int:pk>/', views.resume_delete, name='resume_delete'),
    path('pdf_download/<int:pk>/', views.pdf_download, name='pdf_download'),
]
