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

ix = index.open_dir("indexdir")

queryTest = "plant"
with ix.searcher(weighting = scoring.Frequency) as searcher:
    parser = QueryParser("content", ix.schema)
    myquery = parser.parse(u"" + queryTest)
    results = searcher.search(myquery)

    print(len(results))
    for result in results:
        print(result)