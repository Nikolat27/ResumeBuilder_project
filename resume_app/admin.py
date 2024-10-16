from django.contrib import admin
from .models import Resume, Skill, TechnicalSkill, Experience, Education

admin.site.register(Resume)
admin.site.register(Skill)
admin.site.register(TechnicalSkill)
admin.site.register(Experience)
admin.site.register(Education)
