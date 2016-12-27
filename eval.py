# -*- coding: utf-8 -*-
from gensim.models import word2vec as wv
from indicnlp.morph import unsupervised_morph 
from indicnlp import common
from indicnlp.tokenize import indic_tokenize 
import numpy as np
import sys

wordtovec = wv.Word2Vec.load("LWindow/Word2Vec"+str(sys.argv[1]))
morphtovec = wv.Word2Vec.load("LWindow/Morph2Vec"+str(sys.argv[1]))

lhs1 = unicode('பில்லியன்கள்','utf-8')
lhs2 = unicode('பல','utf-8')
lhs3 = unicode('சில','utf-8')
rhs = unicode('மில்லியன்கள்','utf-8')

m1 = unicode('பில்லியன்','utf-8')
m2 = unicode('மில்லியன்','utf-8')

print '\n\n\t\t\t\t..............................\n\t\t\t\t\t\t'+str(sys.argv[1])+'\n\t\t\t\t..............................\n'

wres = np.sum(np.absolute((np.array(wordtovec[lhs1]) - np.array(wordtovec[lhs2]) + np.array(wordtovec[lhs3])) - np.array(wordtovec[rhs])))

print 'Word2Vec Error: ', wres/float(250)

mres = np.sum(np.absolute((np.array(morphtovec[m1]) - np.array(morphtovec[lhs2]) + np.array(morphtovec[lhs3])) - np.array(morphtovec[m2])))

print 'Morph2Vec Error: ', mres/float(250)

lhs1 = unicode('பில்லியன்','utf-8')
lhs2 = unicode('பல','utf-8')
lhs3 = unicode('சில','utf-8')
rhs = unicode('மில்லியன்','utf-8')

print 'Word2Vec Error: ', np.sum(np.absolute((np.array(wordtovec[lhs1]) - np.array(wordtovec[lhs2]) + np.array(wordtovec[lhs3])) - np.array(wordtovec[rhs])))/float(250)
print 'Morph2Vec Error: ', np.sum(np.absolute((np.array(morphtovec[lhs1]) - np.array(morphtovec[lhs2]) + np.array(morphtovec[lhs3])) - np.array(morphtovec[rhs])))/float(250)
print '\n\nWORD2VEC: SIMILARITY (பில்லியன்) and (மில்லியன்):'
print wordtovec.similarity(u'பில்லியன்', u'மில்லியன்')
print 'MORPH2VEC: SIMILARITY (பில்லியன்) and (மில்லியன்):'
print morphtovec.similarity(u'பில்லியன்', u'மில்லியன்')
print '\n\nWORD2VEC: MOST SIMILAR TO பில்லியன்'
print repr([x[0].encode('utf-8') for x in list(wordtovec.most_similar(positive=[u'பில்லியன்']))]).decode('string-escape')
print 'MORPH2VEC: MOST SIMILAR TO பில்லியன்'
print repr([x[0].encode('utf-8') for x in list(morphtovec.most_similar(positive=[u'பில்லியன்']))]).decode('string-escape')
