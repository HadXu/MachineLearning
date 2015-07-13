#coding:utf-8
'''
Created on 2015年7月6日

@author: Administrator
'''
from gensim import corpora, models, similarities
documents = ["Human machine interface for lab abc computer applications",
            "A survey of user opinion of computer system response time",
              "The EPS user interface management system",
            "System and human system engineering testing of EPS",
            "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
            "The intersection graph of paths in trees",
            "Graph minors IV Widths of trees and well quasi ordering",
           "Graph minors A survey"]

# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]
# remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
          for text in texts]

from pprint import pprint   # pretty-printer
#pprint(texts)


dictionary = corpora.Dictionary(texts)
#print dictionary.token2id

new_doc = "Human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())

#print new_vec
corpus = [dictionary.doc2bow(text) for text in texts]
#print corpus

tfidf = models.TfidfModel(corpus)
index = similarities.MatrixSimilarity(tfidf[corpus])
sims = index[tfidf[new_vec]]
i =  sorted(list(enumerate(sims)),key=lambda x:-x[1])[1][0] 
print documents[i]








