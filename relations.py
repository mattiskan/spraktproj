import nltk, re
from triple import *

#grammar = "Relation: {<N.*><V.*><NNP>}"

grammar = r"""
  NP: {<DT>?<JJ>?<NN.*>+}          # Chunk sequences of DT, JJ, NN
  VB: {<VB.*>} # Chunk verbs and their arguments
  REL: {<NP><VB><NP>}           # Chunk NP, VP
  """

cp = nltk.RegexpParser(grammar,loop=2)


def getRelations(sentences):
    results = []
    tagged_sents = sentences
    #for s in sentences:
    #    tagged_sents.append(nltk.pos_tag(s))
    for sent in tagged_sents:
        tree = cp.parse(sent)
        for subtree in tree.subtrees():
            if subtree.label() == 'REL':
                A = [subtree.leaves()[0]]
                R = subtree.leaves()[1:-1]
                B = [subtree.leaves()[-1]]
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
