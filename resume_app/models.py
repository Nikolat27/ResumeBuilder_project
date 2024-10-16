from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="resume", null=True, blank=True)
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    profile = models.TextField()

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    resume = models.ForeignKey(Resume, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class TechnicalSkill(models.Model):
    resume = models.ForeignKey(Resume, related_name='technical_skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Experience(models.Model):
    resume = models.ForeignKey(Resume, related_name='experiences', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    description = models.TextField()
    dates = models.CharField(max_length=50)  # e.g., "2005-2007"

    def __str__(self):
        return f"{self.role} at {self.company_name}"


class Education(models.Model):
    resume = models.ForeignKey(Resume, related_name='educations', on_delete=models.CASCADE)
    university_name = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    gpa = models.CharField(max_length=10)  # You may want to use FloatField instead for actual GPA

    def __str__(self):
        return f"{self.major} from {self.university_name}"
