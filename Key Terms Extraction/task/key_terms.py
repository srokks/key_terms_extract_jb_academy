# Write your code here
import string

import nltk
import pandas as pd
from lxml import etree
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer


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
def remove_nouns(words_dict):
    for head in words_dict:
        temp_list = []
        for item in words_dict[head]['lemms']:
            if nltk.pos_tag([item])[0][1] == 'NN':
                temp_list.append(item)
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



def gen_tfid(words_dict):
    dataset = [' '.join(sorted(words_dict[head]['lemms'],reverse=True)) for head in words_dict]
    pass
    vectorizer = TfidfVectorizer()
    tfidf_vectorizer_vectors=vectorizer.fit_transform(dataset)
    tf_id_col = []
    for el in tfidf_vectorizer_vectors: # for every vector
        first_vector_tfidfvectorizer = el
        df = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(), index=vectorizer.get_feature_names_out(),
                      columns=["tfidf"])
        df = df.sort_values(by=["tfidf"],ascending=False)
        tf_idf = {}
        for word, tfidf in df.iterrows():
            if tfidf.values[0] != 0:
                tf_idf.update({word:tfidf.values[0]})
        tf_id_col.append(tf_idf)
    for pos,head in enumerate(words_dict):
        words_dict[head].update({'tfid':tf_id_col[pos]})

parsed_text_dict = parse_from_xml()
tokenize(parsed_text_dict)
lemmatize(parsed_text_dict)
remove_not_words(parsed_text_dict)
remove_nouns(parsed_text_dict)
gen_tfid(parsed_text_dict)

# most_freq_nn(parsed_text_dict)

# print_most_frex_words(parsed_text_dict)
