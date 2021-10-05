import PyPDF2, nltk
from pathlib import Path
from time import perf_counter
import json

def timer_decorator(func):
    """
    Prints execution time of func to console.
    """
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        ret_val = func(*args, **kwargs)
        end_time = perf_counter()
        print(f'-Function \'{func.__name__}\' execution time: {(end_time-start_time)} seconds-')
        return ret_val
    return wrapper

def doc_reader():
    """
    Reads all PDFs in a folder with hardcoded absolute path, and writes text to
    individual .txt files in current working directory.
    """
    pathlist = Path(r'D:\Lokale filer\Admin\Py\lang_proc\Corp').glob('**/*.pdf')
    for path in pathlist:
        str_path = str(path)
        target_name = (str(path.stem) + '.txt')
        with open(str_path, 'rb') as text:
            with open(target_name, 'a', encoding = 'utf-8') as target:
                pdf_reader = PyPDF2.PdfFileReader(text) 
                for x in range(pdf_reader.numPages):
                    page = pdf_reader.getPage(x)
                    target.write(page.extractText())

def nltk_ibsen():
    """
    Returns an nltk plain text corpus containing all texts in the given,
    absolute path directory.
    """
    worklist = nltk.corpus.PlaintextCorpusReader(
                                r'D:\Lokale filer\Admin\Py\lang_proc\Corp\txt',
                                '.*',
                                encoding = 'utf-8')
    return worklist

@timer_decorator
def unique_test(corp, unique_dict):
    """
    Tests whether any work in an nltk plaintext corpus, corp, contains any
    string in dictionary unique_dict. Prints warning to console for
    duplicate words. Returns a set of tested unique words.
    """
    cleanup_list = [l for subl in unique_dict.values() for l in subl]   
    for idx, word in enumerate(cleanup_list):
        counter = 0
        for fid in corp.fileids():
            if word in corp.words(fid):
                counter += 1
                print(f'{word} found in {fid}')
        if counter > 1:
            del cleanup_list[idx]
            print(f'-\'{word}\' duplicate found and removed.-')
    return set(cleanup_list)

@timer_decorator
def unique_words(corp):
    """
    Returns a dictionary of text name: unique words in nltk plain text corpus,
    corp.
    """

    def make_readable(the_title):
        """
        Returns a more readable form of a title from an nltk plain text
        corpus, the_title.
        """
        stripped = the_title.replace('.txt', '').replace('_', ' ')
        word_list = [w.capitalize() if
                        (len(w) > 3) else
                        w for w in str(stripped).split(' ')
                        ]
        word_list[0] = word_list[0].capitalize()        
        return ' '.join(word_list).replace(
                                    ' 1', ', første versjon').replace(
                                    ' 2', ', andre versjon').replace(
                                    ' 3', 'tredje versjon'
                                    )
    big_list = []
    full_dict = {}
    unique_dict = {}
    for fid in corp.fileids():
        print(f'Reading {fid}')
        all_words = set([w.lower() for w in corp.words(fid)])
        readable_name = make_readable(fid)
        full_dict[readable_name] = all_words
        big_list.append(all_words) 
    fdist2 = nltk.FreqDist([w for sublist in big_list for w in sublist])
    for key, value in full_dict.items():
        unique_dict[key] = [w for w in value if
                                            (fdist2[w] == 1)
                                            and w.isalpha()
                                            and not w.endswith('-')
                                            and (len(w) > 3)
                                            ]   
    return unique_dict

def word_picker(word_dict):
    """
    Currently prints (but later may return, depending on use) a random
    key: value pair from word_dict.
    """
    key_list = [k for k in word_dict.keys()]
    choice_key = key_list[(randint(0, len(key_list)-1))]
    choice_value = word_dict[choice_key][randint(0, (len(word_dict[choice_key])-1))]
    print(f'{choice_value} chosen at random from {choice_key}')

def json_writer(unique_dict):
    """
    Dumps a dictionary, unique_dict, to a json file.
    """
    with open('ibsen_unique_words.json', 'w') as out_file:
        json.dump(unique_dict, out_file)

if __name__ == '__main__':
#   doc_reader()
#   ibsen_corpus = nltk_ibsen()
#   uniques = unique_words(ibsen_corpus)
#   json_writer(uniques)
#   unique_test(ibsen_corpus, uniques)
#   print(sum(len(l) for l in uniques.values()))
    with open('ibsen_unique_words.json') as json_file:
        word_picker(json.load(json_file)) #TA-DAH!