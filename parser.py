#!/usr/bin/python3
import nltk
from nltk.stem import WordNetLemmatizer

def read_file(fname):
    data = ""
    with open(fname, 'r') as myfile:
        data=myfile.read().replace('\n', '')

    return data
            

def get_sentences(data):
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    return sent_detector.tokenize(data);


class_map = {'JJ': 'a', 'VB':'v', 'NN':'n', 'RB': 'r'}
stemmer = WordNetLemmatizer()

def stem(word, cls):
    cls = cls[:2]
    if(cls in class_map and STEM):
        return stemmer.lemmatize(word, class_map[cls]).lower()
    else:
        return word.lower()

def classify_text(data):
    words = nltk.word_tokenize(data)

    return nltk.pos_tag(words)


data = read_file("simple.txt")
STEM = True

sentences = get_sentences(data)

words = sum([ classify_text(sentence) for sentence in sentences ], [])


classified_words = {}

for cls in ['NN', 'VB', 'DT', 'IN', 'JJ', 'CC']:
    classified_words[cls] = set()
    for word in words:
        if word[1].startswith(cls):
            classified_words[cls].add( stem(word[0], cls) )
    

for cls,words in classified_words.items():
    print()
    print(cls[0], "-> ", end="")
    for word in words:
        print("'", word, "' | ", sep="", end="")

print("\nEND -> ',' | '.' | '-' | '?' | '!'")

