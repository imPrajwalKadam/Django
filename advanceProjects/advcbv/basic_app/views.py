from typing import Any
from django.shortcuts import render
from django.views.generic import View
from django.views.generic import View,TemplateView,ListView,DetailView
from .import models


class indexView(TemplateView):
        template_name = 'index.html'
        
class SchoolListView(ListView):
          context_object_name = 'schools'
          model = models.School


class SchoolDetailView(DetailView):
        context_object_name = 'school_detail'
        model = models.School
        template_name = 'basic_app/school_detail.html'

