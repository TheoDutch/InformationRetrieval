# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:12:03 2018

@author: tpayer
"""
from whoosh import index
from whoosh.fields import *
from tqdm import tqdm
from whoosh.qparser import QueryParser
from whoosh import scoring
from extract_queries import extract_topics
from string import Template
import os


ix = index.open_dir("indexdir")

topic_list = extract_topics()

#%%
'''
queryTest = "plant"
with ix.searcher(weighting = scoring.Frequency) as searcher:
    parser = QueryParser("content", ix.schema)
    myquery = parser.parse(u"" + queryTest)
    results = searcher.search(myquery)

    print(len(results))
    for result in results:
        print(result)
'''      
#%%        
        
result_list = []
with ix.searcher(weighting = scoring.TF_IDF()) as searcher:
    parser = QueryParser("content", ix.schema)
    for i, row in topic_list.iterrows():
        print(i)
        query = parser.parse(u"" + row["title"])
        # this search only gives the top-10 
        results = searcher.search(query)
        #print(len(results))
        topic_number = row['topic_number']
        for result in results:
            results_ = {}
            results_['topic_no'] = topic_number
            results_['docno'] = result['docno']
            results_['path'] = result['path']
            results_['rank'] = result.rank
            results_['score'] = result.score
            result_list.append(results_)
#%%        
# creating a string template for the eval file        
t = Template('$topic_number Q0 $docno $rank $score IR_group6')

eval_format = []
for result in result_list:
    #file = os.path.basename(os.path.normpath(result['path']))
    #doc_no = result['docno']
    foo = t.substitute(topic_number=result['topic_no'], docno=result['docno'], rank=result['rank'], score=result['score'])
    eval_format.append(foo)

#%%
with open('query_results.txt', 'w') as f:
    for item in eval_format:
        f.write("%s\n" % item)
