#!/usr/local/bin/python
import nltk, re, pprint
import triple.py
from nltk.corpus import reuters
from nltk.sem import relextract,extract_rels,rtuple

grammar = "Relation: {<DT>?<JJ>*<NN><V.*><NN>}"


cp = nltk.RegexpParser(grammar)
s = [nltk.pos_tag(s) for s in reuters.sents()[:30]]

#print sentence
#print cp.parse(sentence)
#nltk.ne_chunk


brown = nltk.corpus.brown #
for sent in s:
	tree = cp.parse(sent)
	for subtree in tree.subtrees():
   		if subtree.label() == 'Relation':
   			print(tree) 
   			print(subtree.leaves())
'''#

IN = re.compile(r'.*\bof\b.*')

for i,sent in enumerate(s):
	sent = nltk.ne_chunk(sent)
	rels = extract_rels('PERSON','ORGANIZATION',doc=sent,corpus='ace',pattern=IN,window=7)
	for rel in rels: print('{0:<5}{1}'.format(i, rtuple(rel)))

#'''