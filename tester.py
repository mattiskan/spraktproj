import nltk
from relations import *
from nltk.corpus import reuters
from nltk.corpus import gutenberg

#test with n sentences from reuters
def testRelations(n=1500):
	sents = []
	f = open('testData.txt', 'rU')
	for line in f:
		sents.append(nltk.word_tokenize(line))
	#sents = [s for s in gutenberg.sents('carroll-alice.txt')[:n]]
	results = getRelations(sents)
	print()

	for i, rel in enumerate(results):
		print rel
testRelations()