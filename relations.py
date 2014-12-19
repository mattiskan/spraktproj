import nltk, re
from triple import *

grammar = "Relation: {<N.*><V.*><NNP>}"
cp = nltk.RegexpParser(grammar)

def getRelations(sentences):
        results = []
        tagged_sents = [nltk.pos_tag(s) for s in sentences]
        for sent in tagged_sents:
                tree = cp.parse(sent)
                for subtree in tree.subtrees():
                        if subtree.label() == 'Relation':
                                A = [subtree.leaves()[0]]
                                R = subtree.leaves()[1:-1]
                                B = [subtree.leaves()[-1]]
                                results.append(Triple(A,R,B))
        return results
