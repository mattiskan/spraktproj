import nltk
from relations import *
from nltk.corpus import reuters

#test with n sentences from reuters
def testRelations(n=100):
	sents = [s for s in reuters.sents()[:n]]
	results = getRelations(sents)
	for i, rel in enumerate(results[:5]):
		print rel

testRelations()