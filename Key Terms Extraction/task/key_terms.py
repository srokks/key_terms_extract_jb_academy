# Write your code here
from lxml import etree
from nltk import word_tokenize
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
                tail = elle.text
        parsed_text_dict.update({head: tail})
    return parsed_text_dict

def gen_tokens(text):
    return sorted(word_tokenize(text.lower()),reverse=True)

def gen_most_freq_words(parsed_text_dict):
    for head,tail in parsed_text_dict.items():
        tokens = gen_tokens(tail)
        parsed_text_dict[head] = Counter(tokens).most_common(5)

def tokenize(words_dict):
    for head in words_dict:
        words_dict[head].update({'tokens':word_tokenize(words_dict[head]['tail'])})
def lemmatize(words_dict):
    lemm = WordNetLemmatizer()
    for head in words_dict:
        words_dict[head].update({'lemms':[lemm.lemmatize(x) for x  in words_dict[head]['tokens']]})
def remove_not_words(words_dict):
    not_allowed_list = stopwords.words('english')
    not_allowed_list.extend(string.punctuation)
    for head in words_dict:
        temp_list = [item for item in words_dict[head]['lemms'] if item not in not_allowed_list]
        words_dict[head]['lemms'] = temp_list
    # print(stopwords.words('english'))
    # print(list(string.punctuation))
    #removes punctuations
    #print([item for item in a if item not in list(string.punctuation)])
def print_most_frex_words(words_dict):
    for head in words_dict:
        print(f'{head}:')
        # print(tail)
        print(' '.join(([x for x,y in tail])))
        # print(sorted(tail.items(),key= lambda item: item[1],reverse=True))
        # for el in tail[]:
        #     print(el)

# counter = Counter(gen_tokens(test_txt))
parsed_text_dict = parse_from_xml()
gen_most_freq_words(parsed_text_dict)

print_most_frex_words(parsed_text_dict)