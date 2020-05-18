#NGram TF-IDF and Clustering Trials

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans

import pandas as pd
import numpy as np

corpus=["this is a test message",
        "the weather is good",
        "testing weather is good",
        "movie is good",
        "food is not good"]

#To Generate TF-IDF Matrix ( 2 and 3 grams)

vec=TfidfVectorizer(ngram_range=(2,3))
vec_m=vec.fit_transform(corpus)
vec_m=vec_m.toarray()

vocab=vec.get_feature_names()
pd.set_option('display.max_columns', 30)
view_1=pd.DataFrame(np.round(vec_m,2),columns=vocab)

#Use view_1 to print the dataframe


#Pairwise Cosine similarity

sm=cosine_similarity(vec_m)

view_2=pd.DataFrame(sm)

"""
dist = 1 - cosine_similarity()

#print(vec.get_feature_names())

km=KMeans(n_clusters=3).fit_predict(A)
#c=km.labels_.tolist()

"""
