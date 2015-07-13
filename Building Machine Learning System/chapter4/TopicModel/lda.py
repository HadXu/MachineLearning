#coding:utf-8
'''
Created on 2015年7月6日

@author: Administrator
'''
from gensim import corpora, models, similarities
corpus = corpora.BleiCorpus('ap/ap.dat', 'ap/vocab.txt')
model = models.ldamodel.LdaModel(corpus, num_topics=2, id2word=corpus.id2word,alpha=1)

topics = [model [c] for c in corpus]
print sorted(topics[0],key=lambda x: -x[1] )





