import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class ResumeCreationView(View):
    template_name = 'resume_app/resume_creation.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        data = json.loads(request.body)
        
