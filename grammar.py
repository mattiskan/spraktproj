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
    if cls in class_map:
        return stemmer.lemmatize(word, class_map[cls]).lower()
    else:
        return word.lower()

def classify_text(data):
    words = nltk.word_tokenize(data)

    return nltk.pos_tag(words)

data = read_file("simple.txt")

sentences = [ classify_text(sentence) for sentence in get_sentences(data) ]



stemmed_sentences = []

for words in sentences:
    sentence = []
    for word in words:
        sentence += [ stem(word[0], word[1]) ]

    stemmed_sentences += [ sentence ]



#context free grammar
groucho_grammar = nltk.data.load('file:grammar.cfg')
parser = nltk.ChartParser(groucho_grammar)

for sentence in stemmed_sentences:
    try:
        print()
        print(sentence)
        i = 0
        for tree in parser.parse(sentence):
            print(tree)
            i += 1

        print("found ", i)
    except ValueError as x:
        print(x)
