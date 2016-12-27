# Embedding-And-Morphological-Segmentation

This is part of a research project I am conducting on the effects of morphological segmentation on the embedding process using algorithms like Word2Vec.

To run the algorithm, use:
 
    python morph2vec.py 0 <window_size>
    
to run the word2vec algorithm without the morphological segmentation, and

    python morph2vec.py 1 <window_size>
        
to run the word2vec algorithm without the morphological segmentation 

on the corpus present in a newline-separated format in `input`.

To run the evaluation, simply run the same script again triggering the else clause or run:

    python eval.py <window_size>

In order to visualize the embeddings using t-distributed Stochastic Neighbour Embedding technique,

    cd t-SNE/
    #word2vec
    python prep_tSNE.py 0 <window_size>
    
    cd t-SNE/
    #morph2vec
    python prep_tSNE.py 1 <window_size>
    
Additionally, to find out the number of unique words in the corpus (the vocabulary),

    ./word_occurrence_count srcfile wcfile

A sample of implementation code is available in `start.sh`
