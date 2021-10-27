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


def print_most_frex_words(parsed_text_dict):
    for head, tail in parsed_text_dict.items():
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