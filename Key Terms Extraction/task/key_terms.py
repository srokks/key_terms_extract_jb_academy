# Write your code here
import string

from lxml import etree
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter


def parse_from_xml():
    file_name = 'news.xml'
    root = etree.parse(file_name).getroot()
    parsed_text_dict = {}
    for el in root[0]:
        for elle in el:
            if elle.get('name') == 'head':
                head = elle.text
            if elle.get('name') == 'text':
                tail = elle.text.lower()
        parsed_text_dict.update({head: {'tail': tail}})
    return parsed_text_dict


def tokenize(words_dict):
    for head in words_dict:
        words_dict[head].update({'tokens':sorted(word_tokenize(words_dict[head]['tail']),reverse=True)})


def lemmatize(words_dict):
    lemm = WordNetLemmatizer()
    for head in words_dict:
        words_dict[head].update({'lemms': [lemm.lemmatize(x) for x in words_dict[head]['tokens']]})


def remove_not_words(words_dict):
    not_allowed_list = stopwords.words('english')
    not_allowed_list.extend(string.punctuation)
    for head in words_dict:
        temp_list = [item for item in words_dict[head]['lemms'] if item not in not_allowed_list]
        words_dict[head]['lemms'] = temp_list

def most_freq(words_dict):
    for head in words_dict:
        words_dict[head].update({'most_freq':Counter(words_dict[head]['lemms']).most_common(5)})
def print_most_frex_words(words_dict):
    for head in words_dict:
        print(f'{head}:')
        # print(words_dict[head]['most_freq'])
        print(' '.join(([x for x,y in words_dict[head]['most_freq']])))
        # print(sorted(tail.items(),key= lambda item: item[1],reverse=True))
        # for el in tail[]:
        #     print(el)


parsed_text_dict = parse_from_xml()
tokenize(parsed_text_dict)
lemmatize(parsed_text_dict)
remove_not_words(parsed_text_dict)
most_freq(parsed_text_dict)
print_most_frex_words(parsed_text_dict)
pass
