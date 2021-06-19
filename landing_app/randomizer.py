from django.conf import settings
from pathlib import Path
from random import randint
import json

def word_picker(*args, **kwargs):
	"""
	Returns a tuple containing (key, value) where key, then value are
	randomly picked from the specified json file.
	"""
	with open(settings.BASE_DIR / 'static/ibsen_unique_words.json') as json_file:
		word_dict = json.load(json_file)
	key_list = [k for k in word_dict.keys()]
	choice_key = key_list[(randint(0, len(key_list)-1))]
	choice_value = word_dict[choice_key][randint(0, (len(word_dict[choice_key])-1))]
	return (choice_key, choice_value)