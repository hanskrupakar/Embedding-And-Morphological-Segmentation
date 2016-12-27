# -*- coding: utf-8 -*-
from gensim.models import word2vec as wv
from gensim.models import doc2vec as dv
import numpy as np
import random
import re
import os
import string
import sys
from indicnlp.morph import unsupervised_morph 
from indicnlp import common
from indicnlp.tokenize import indic_tokenize 

w=int(sys.argv[2])

if(sys.argv[1]=='1'):
	m='Morph2Vec'
else:
	m='Word2Vec'
if(not os.path.exists("embedding/"+m+str(w))):
	print("\t\t     creating "+m+" vectors for Tamil")
	if(not os.path.exists(m+".TA")):
		with open("input", "r") as f:
		    tam = f.read()
		print("     Tamil file read complete")
		tam = re.sub(r'['+re.escape(string.punctuation)+'a-zA-Z0-9]', '',tam)
		print("     Removed punctuation and non-native characters")
		if(sys.argv[1]=='1'):
		
			common.INDIC_RESOURCES_PATH="/opt/indic_nlp_library/indic_nlp_resources"

			analyzer=unsupervised_morph.UnsupervisedMorphAnalyzer('ta')

			s=''

			for line in tam.split('\n'):
				if line.strip():
					tokens=analyzer.morph_analyze_document(line.decode('utf-8').strip().split(' '))
					s += ' '.join(tokens).strip().encode('utf-8') + '\n'
			tam=s
			print("     Morphological analysis complete")

		with open(m+'.TA', 'w+') as f:
			f.write(tam)
	else:
		with open(m+'.TA', 'r') as f:
			tam = f.read()
		
	sent=[]
	twv=[]
	for e in unicode(tam, "utf-8").split("\n"):
	    twv.append(indic_tokenize.trivial_tokenize(e))
	twv=filter(None,twv)
	print("     Input ready for "+m+" algorithm, Starting...")
	modeltam = wv.Word2Vec(twv, size=100, window=w, workers=1, batch_words=25, min_count=1)
	modeltam.save("embedding/"+m+str(w))

	print("     "+m+" model created and saved successfully!")

else:        
	os.system("eval.py "+str(w))

'''
    	modeltam = wv.Word2Vec.load("Same Window/"+m)
	#modeltam = wv.Doc2Vec.load("embedding/"+m)
    	print(modeltam[unicode("ராஜாவாகிய","utf-8")])

def decode(x, n, vs):
    modeltam = wv.Word2Vec.load("embedding/word2vec_vocab%d_%d.TA" % (vs,n))
    print(np.reshape(modeltam.similar_by_vector(x)[0], vs))


Gensim Word2Vec Arguments: 

min count: threshold count for ignoring words
size: dimensionality of feature vectors
workers: parallelization (no of threads)
window: centre + window/2 elements on either side of the window
alpha: initial learning rate
max_vocab_size: threshold the vocabulary (prunes infrequent ones)
sample: probability threshold to downsample too frequent words (0 to 10^-5) [directly proportional to frequent words reduction]
sg: 0 - CBOW, 1 - Skip-Gram
hs: 1 - Hierarchical Softmax, 0 - Negative Sampling if negative==1
negative=n: n>0 - Negative Sampling (5 to 20 usually) no. of noise words, 0 - no Negative Sampling 
cbow_mean: if CBOW, 0: sum context word vectors, 1: mean context word vectors
hashfxn: hash function to use to randomly initialize weights, for increased training reproducibility
iter: no of iterations over the corpus.
trim_rule: vocabulary trimming rule, specifies whether certain words should remain in the vocabulary, be trimmed away, or handled using the default [applies iff word count > min_count]
sorted_vocab: if 1 (default), sort the vocabulary by descending frequency before assigning word indexes.
batch_words: target size (in words) for batches of examples passed to worker threads
'''
