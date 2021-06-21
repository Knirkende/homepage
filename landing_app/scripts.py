from django.conf import settings
from pathlib import Path
from random import randint
import json
from bs4 import BeautifulSoup
import requests
import lxml
import re

def _wiki_lookup(name, *args, **kwargs):
	"""
	Returns the first paragraph of the Norwegian wikipedia article on a given
	work of literature by Henrik Ibsen. Strips footnote markers.
	"""
	lookup_name = name.replace(
						'første versjon', '').replace(
						'andre versjon', '').replace(
						'tredje versjon', '').replace(
						',', '').replace(' ', '_')
	if lookup_name == 'Catilina':
		lookup_name =='Catilina_(drama)'
	elif lookup_name == 'Kongs-emnerne':
		lookup_name == 'Kongs-Emnerne'
	elif lookup_name == 'De_Unges_Forbund':
		lookup_name.replace('U', 'u')
	elif lookup_name == 'Kjæmpehøien':
		lookup_name.replace('i', 'j')
	URL = "https://no.wikipedia.org/wiki/" + lookup_name
	r = requests.get(URL)
	soup = BeautifulSoup(r.content, 'lxml')
	try:
		cont = soup.find('div', class_='mw-parser-output')
		parag = re.sub('\[\d\]', '', cont.find('p').get_text())
	except AttributeError:
		return f'Fant ingen artikkel om {name} på norsk wikipedia. Forsøkte {URL}.'
	return parag

def word_picker(*args, **kwargs):
	"""
	Returns a tuple containing (key, value, wiki paragraph) where key,
	then value are randomly picked from the specified json file.
	"""
	with open(settings.BASE_DIR / 'static/ibsen_unique_words.json') as json_file:
		word_dict = json.load(json_file)
	key_list = [k for k in word_dict.keys()]
	choice_key = key_list[(randint(0, len(key_list)-1))]
	choice_value = word_dict[choice_key][randint(0, (len(word_dict[choice_key])-1))]
	info_paragraph = _wiki_lookup(name = choice_key)
	return (choice_key, choice_value, info_paragraph)