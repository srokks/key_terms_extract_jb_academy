# key_terms_extract_jb_academy

## Info

Key terms extract project from <a href="https://hyperskill.org/projects/166?track=2">JetBrainAcademy Python Learning Track</a>.
Script reads articles from **XML** file and process it -  lowercase the text, tokenize it with the **NLTK** tokenizer's help, and create a token frequency list.
After It is applying lemmatization and deleting stop-words, digits, and punctuation. Using **POS tagging** removes nouns.
Finally generates **TF-IDF** for each last word and returns five most frequent words. 
### Prerequisites

To run code you'll need have installed modules 
**ntlk**,**pandas**,**lxml**,**sklearn**
## Run
In key_terms.py file localization
```sh
python3 key_terms.py
```
