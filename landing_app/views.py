from django.shortcuts import render

from django.views.generic import TemplateView

class LandingPage(TemplateView):
	template_name = 'landing_app/base.html'