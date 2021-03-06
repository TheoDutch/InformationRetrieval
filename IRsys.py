# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 09:07:57 2018

@author: tpijkeren
"""
from whoosh import index
from whoosh.fields import *
from whoosh.query import *
import os.path
from os.path import isfile, join
from os import listdir
from whoosh.qparser import QueryParser
from bs4 import BeautifulSoup
import codecs
import frogress
import re
from whoosh import scoring
from whoosh.lang.porter import stem

#dingen van Theo
#datapath = '/mnt/HDD/latimes/'
#datapath = 'testdata/'

#ding van Kimberly
datapath = "/Users/kimberlystoutjesdijk/Desktop/index/"

laptopVanKimberlyDoetMoeilijk = True

def get_schema():
    return Schema(docno=ID(unique=True, stored=True),
    headline=TEXT(stored=True), path=ID(stored=True), content=TEXT)

def striptags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def add_doc(writer, path):
    infile = open(path,"r").read()
    infile = '<root>'+infile+'</root>'
    if laptopVanKimberlyDoetMoeilijk:
        soup = BeautifulSoup(infile, 'html.parser')
        docs = soup.find_all('doc')
        for doc in docs:
            docno = unicode(striptags(str(doc.docno)), "utf-8")
            headline = unicode(striptags(str(doc.headline)),"utf-8")  # yes, this works, please dont change
            text = unicode(striptags(str(doc.text)),"utf-8")
            writer.add_document(docno=docno, headline=headline, path=path, content=text)
    else:
        soup = BeautifulSoup(infile, 'xml')
        docs = soup.find_all('DOC')
        for doc in docs:
            docno = unicode(striptags(str(doc.DOCNO)), "utf-8")
            headline = unicode(striptags(str(doc.HEADLINE)), "utf-8")  # yes, this works, please dont change
            text = unicode(striptags(str(doc.TEXT)), "utf-8")
            writer.add_document(docno=docno, headline=headline, path=path, content=text)

def clean_index(dirname):
    # Always create the index from scratch
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    print(dirname, get_schema())
    ix = index.create_in(dirname, get_schema())
    writer = ix.writer()

    doclist = [f for f in listdir(datapath) if isfile(join(datapath, f))]
    # Assume we have a function that gathers the filenames of the
    # documents to be indexed
    #for path in my_docs():
    l = len(doclist)
    #for i, filename in enumerate(doclist):
    for filename in frogress.bar(doclist):
        add_doc(writer, u""+datapath + filename)
    writer.commit()

#==============================================================================
# schema = Schema(title=TEXT(stored=True), content=TEXT) # stored shows in results
# ix = index.create_in("index", schema)
# #ix = open_dir("index")
# writer = ix.writer()
# writer.add_document(title=u"My document", content=u"This is my document!")
# writer.add_document(title=u"Second try", content=u"This is the second example.")
# writer.add_document(title=u"Third time's the charm", content=u"Examples are many.")
# writer.commit()
#==============================================================================

#clean_index("latimes_indexed")
ix = index.open_dir("latimes_indexed")
# searcher = ix.searcher()
# parser = QueryParser("content", ix.schema)
# myquery = parser.parse(u"plants")
# results = searcher.search(myquery)
#
# print(len(results))
# for result in results:
#     print(result)
# searcher.close()


#scoring.BM25F(B=0.75, K1=1.5) -> nog uitzoeken wat die parameters precies doen, in de documentation staat alleen 'see literature'
#scoring.TF_IDF()
#scoring.Frequency
queryTest = "plant"
with ix.searcher(weighting = scoring.Frequency) as searcher:
    parser = QueryParser("content", ix.schema)
    myquery = parser.parse(u"" + queryTest)
    results = searcher.search(myquery)

    print(len(results))
    for result in results:
        print(result)

    #The results file has the format: query_id, iter, docno, rank, sim, run_id  delimited by spaces.
    # Query id is the query number (e.g. 136.6 or 1894, depending on the evaluation year).
    # The iter constant, 0, is required but ignored by trec_eval.
    # The Document numbers are string values like FR940104-0-00001 (found between <DOCNO> tags in the documents).
    # The Similarity (sim) is a float value.
    # Rank is an integer from 0 to 1000, which is required but ignored by the program.
    # Runid is a string which gets printed out with the output.
    for i in range (len(results)):
        with open("results.txt", "a") as f:
            f.write("query id hier " + " " + str(0) + " " + str(results[i].get("docid")) + " " + str(10-i) + " " + str(0) + " " + "bla" + "\n")

#https://whoosh.readthedocs.io/en/latest/stemming.html
#^ voor stemming, nog checken of hij dit ook doet voor het indexen
