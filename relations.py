import nltk, re
from triple import *

grammar = "Relation: {<N.*>+<V.*><DT>?<NNP>+}"
cp = nltk.RegexpParser(grammar)

def getRelations(sentences):
    results = []
    tagged_sents = [nltk.pos_tag(s) for s in sentences]
    tagged_sents = filter(lambda s: s != [], tagged_sents)

    for sent in tagged_sents:
        tree = cp.parse(sent)

        for subtree in tree.subtrees():
            if subtree.label() == 'Relation':

                words = subtree.leaves()

                A = []
                i=0
                while words[i][1].startswith('N'):
                        A.append(words[i])
                        i += 1

                R = []
                while not words[i][1].startswith('N'):
                        R.append(words[i])
                        i += 1                        
                
                B = words[i:]
                            
                results.append(Triple(A,R,B))
    return results

def parseFile(fileName, n=1500):
    sents = []
    f = open(fileName, 'rU')
    for line in f:
        sents.append(nltk.word_tokenize(line))
    #sents = [s for s in gutenberg.sents('carroll-alice.txt')[:n]]
    results = getRelations(sents)
    

    return results
