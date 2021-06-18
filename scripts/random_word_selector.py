from random import randint
from ibs_corpus_maker import timer_decorator

@timer_decorator
def word_picker(word_dict):
	key_list = [k for k in word_dict.keys()]
	choice_key = key_list[(randint(0, len(key_list)-1))]
	choice_value = word_dict[choice_key][randint(0, (len(word_dict[choice_key])-1))]
	print(f'{choice_value} chosen at random from {choice_key}')