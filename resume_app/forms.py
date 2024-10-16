from django import forms
from .models import Resume, Skill, TechnicalSkill, Experience, Education


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ['resume']


class TechnicalSkillForm(forms.ModelForm):
    class Meta:
        model = TechnicalSkill
        exclude = ['resume']


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        exclude = ['resume']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ['resume']
