import nltk
from nltk.corpus import conll2000,brown

grammar = r"""
NP: {<DT|PP\$>?<JJ>*<NN>}
	{<NP>+}
	{<NN>+}
VB: {<V.*>}
Rel: {<NP><VB><NP>}
"""
cp = nltk.RegexpParser(grammar)


class ChunkParser(nltk.ChunkParserI): 
	def __init__(self, train_sents):
		train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)] for sent in train_sents]
		self.tagger = nltk.TrigramTagger(train_data)
	
	def parse(self, sentence):
		pos_tags = [pos for (word,pos) in sentence]
		tagged_pos_tags = self.tagger.tag(pos_tags)
		chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
		conlltags = [(word, pos, chunktag) for ((word,pos),chunktag) in zip(sentence, chunktags)]
		return nltk.chunk.conlltags2tree(conlltags)


test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])

Chunker = ChunkParser(train_sents)

#print(Chunker.evaluate(test_sents))

sents = [s for s in brown.tagged_sents()[100:200]]
for s in sents:
	tree = cp.parse(s)
	for sub in tree.subtrees():
		if sub.label() == 'Rel':
			print(sub)