import json
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Resume, Skill, TechnicalSkill, Experience, Education
from . import forms


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class ResumeCreationView(View):
    template_name = 'resume_app/resume_creation.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        data = json.loads(request.body)
        full_name = data.get("fullName")
        position = data.get("position")
        email = data.get("email")
        phone = data.get("phone")
        profile = data.get("profile")

        resume_instance = Resume.objects.create(user=request.user, full_name=full_name,
                                                position=position, email=email, phone_number=phone, profile=profile)
        for skill in data.get("skills", []):
            skill_form = forms.SkillForm(skill)
            if not skill_form.is_valid():
                return JsonResponse(skill_form.errors, status=400)
            skill_instance = skill_form.save(commit=False)
            skill_instance.resume = resume_instance
            skill_instance.save()

        for technical_skill in data.get("technicalSkills", []):
            technical_skill_form = forms.TechnicalSkillForm(technical_skill)
            if not technical_skill_form.is_valid():
                return JsonResponse(technical_skill_form.errors, status=400)
            technical_skill_instance = technical_skill_form.save(commit=False)
            technical_skill_instance.resume = resume_instance
            technical_skill_instance.save()

        for experience in data.get("experiences", []):
            print(experience)
            experience_form = forms.ExperienceForm(experience)
            if not experience_form.is_valid():
                return JsonResponse(experience_form.errors, status=400)
            experience_instance = experience_form.save(commit=False)
            experience_instance.resume = resume_instance
            experience_instance.save()

        for education in data.get("educations", []):
            education_form = forms.EducationForm(education)
            if not education_form.is_valid():
                return JsonResponse(education_form.errors, status=400)
            education_instance = education_form.save(commit=False)
            education_instance.resume = resume_instance
            education_instance.save()

        return JsonResponse({"message": "Resume created successfully!"}, status=201)


def all_resumes(request):
    resumes = Resume.objects.filter(user=request.user)
    return render(request, "resume_app/all_resumes.html", context={"resumes": resumes})


def retrieve_resume(request, pk):
    resume_instance = Resume.objects.get(id=pk)

    technical_skills1 = resume_instance.technical_skills.all()[:3]
    technical_skills2 = resume_instance.technical_skills.all()[3:6]
    technical_skills3 = resume_instance.technical_skills.all()[6:9]

    context = {
        'technical_skills1': technical_skills1,
        'technical_skills2': technical_skills2,
        'technical_skills3': technical_skills3,
        'resume': resume_instance
    }
    return render(request, "resume_app/resume_detail.html", context)
