# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:57:13 2018

@author: tpayer
"""

import os, os.path
from whoosh import index
#import whoosh.index as index
from whoosh.fields import *
import glob
from bs4 import BeautifulSoup
# import frogress # frogress.bar no longer available??
from tqdm import tqdm
from whoosh.writing import AsyncWriter
import re
from whoosh.writing import BufferedWriter


def striptags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data).strip()

# define a schema for the indexer
def get_schema():
    return Schema(docno=ID(unique=True, stored=True),
    headline=TEXT(stored=True), path=ID(stored=True), content=TEXT)
    

def add_doc(writer, path):
    infile = open(path,"r").read()
    infile = '<root>'+infile+'</root>'
    #print(path)
    #print(len(infile))
    soup = BeautifulSoup(infile, 'xml')
    docs = soup.find_all('DOC')
    for doc in docs:
        docno = striptags(str(doc.DOCNO))
        headline = striptags(str(doc.HEADLINE))  # yes, this works, please dont change <- no it doesn't
        text = striptags(str(doc.TEXT))
        writer.add_document(docno=docno, headline=headline, path=path, content=text)
            
def index_TREC_ROBUST_04():
    schema = get_schema()
    # create an index in the "indexdir" directory.
    if not os.path.exists("indexdir"):
        os.mkdir("indexdir")
        
    ix = index.create_in("indexdir", schema)
    ix = index.open_dir("indexdir")
    
    # creating the index writer (if fasil use AsyncWriter 
    # (https://whoosh.readthedocs.io/en/latest/api/writing.html#whoosh.writing.AsyncWriter))
    # writer = ix.writer()
    writer = ix.writer()#BufferedWriter(ix, period=120, limit=20)
    
    dir_list = ['latimes', 'fbis', 'fr94', 'ft']
    doclist = []
    [doclist.extend(glob.glob(os.path.join(".", "data", source, "*"))) for source in dir_list]
    
    # was frogress.bar instead of tqdm            
    for filename in tqdm(doclist):
        add_doc(writer, filename)
    writer.commit()


if __name__ == '__main__':
    # this function will automatically index the files needed for TREC_Robust_2004
    index_TREC_ROBUST_04()

