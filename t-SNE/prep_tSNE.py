 # -*- coding: utf-8 -*-
from gensim.models import Word2Vec as wv
import tsne
import numpy as np
import pylab

modeltam = wv.load("../Same Window/Word2Vec")
X2 = tsne.bh_sne(np.array(modeltam.syn0[:200,:].tolist()))
Labels =  modeltam.index2word[:200]
print type(Labels[0])
font = { 'fontname':'Arial', 'verticalalignment': 'top', 'horizontalalignment':'center' }
pylab.subplots_adjust(bottom =0.1)
pylab.scatter(X2[:,0], X2[:,1], marker = ',' ,cmap = pylab.get_cmap('Spectral'))
for label, x, y in zip(Labels, X2[:,0], X2[:,1]):
    pylab.annotate(
        label, 
        xy = (x, y), xytext = None,
        ha = 'right', va = 'bottom', **font)
        #,textcoords = 'offset points',bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        #arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
pylab.title('t-SNE')

pylab.savefig('Word2Vec', bbox_inches ='tight', dpi = 1000, orientation = 'landscape', papertype = 'a0')
pylab.close()
