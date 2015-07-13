#coding:utf-8
'''
Created on 2015年7月5日

@author: Administrator
'''

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import load_mlcomp
import nltk.stem

MLCOMP_DIR = r'data'
data = load_mlcomp('20news-18828', mlcomp_root=MLCOMP_DIR)
#print (data.filenames)
#print len(data.filenames)
#print len(data.target_names)

groups = ['comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.ma c.hardware', 'comp.windows.x', 'sci.space']
train_data = load_mlcomp('20news-18828', 'train',mlcomp_root=MLCOMP_DIR,categories=groups)
test_data = load_mlcomp('20news-18828', 'test',mlcomp_root=MLCOMP_DIR)

#print len(test_data.filenames)

english_stemmer = nltk.stem.SnowballStemmer('english')
class StemmedTfidfVectorizer(TfidfVectorizer):
    def bulid_analyzer(self):
        analyzer = super(TfidfVectorizer,self).bulid_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

vectorizer = StemmedTfidfVectorizer(min_df=10, max_df=0.5,stop_words='english',decode_error='ignore')
vectorized = vectorizer.fit_transform(data)
num_samples, num_features = vectorized.shape
print vectorized


from sklearn.cluster import KMeans
#km = KMeans(n_clusters=5, init='random', n_init=1, verbose=1)
#km.fit(vectorized)

#print km.labels_.shape



