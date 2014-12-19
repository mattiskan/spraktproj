import nltk
from relations import *
from nltk.corpus import brown
from nltk.corpus import gutenberg

#test with n sentences from reuters
def testRelations(n=4000):
	'''sents = []
	f = open('testData.txt', 'rU')
	for line in f:
		sents.append(nltk.word_tokenize(line))'''
	sents = [s for s in brown.tagged_sents()[n:2*n]]
	results = getRelations(sents)

	print(len(results))
	#for i, rel in enumerate(results):
	#	print rel

testRelations()