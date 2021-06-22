from django.shortcuts import render
from landing_app.scripts import word_picker

from django.views.generic import TemplateView

class LandingPageView(TemplateView):
	template_name = 'landing_app/base.html'

def ibsen_view(request):
	if request.method == 'GET':	
		title, word, description, url = word_picker()
	return render(request, 'landing_app/landing_page.html', {
		'title': title,
		'word': word,
		'description': description,
		'source': url
		})
