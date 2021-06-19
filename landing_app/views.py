from django.shortcuts import render
from landing_app.randomizer import word_picker

from django.views.generic import TemplateView

class LandingPageView(TemplateView):
	template_name = 'landing_app/base.html'

def ibsen_view(request):
	if request.method == 'GET':	
		test1, test2 = word_picker()
	return render(request, 'landing_app/base.html', {'test1': test1, 'test2': test2})
