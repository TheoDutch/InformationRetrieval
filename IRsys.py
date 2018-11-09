# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 09:07:57 2018

@author: tpijkeren
"""
from whoosh import index
from whoosh.fields import *
from whoosh.query import *
import os.path
from whoosh.qparser import QueryParser
import codecs

def get_schema():
  return Schema(path=ID(unique=True, stored=True), content=TEXT)

def add_doc(writer, path):
  #fileobj = open(path, "rb")
  #content = fileobj.read()
  #fileobj.close()
  
  with codecs.open(path, "r","utf-8") as f:
      content = f.read()
  writer.add_document(path=path, content=content)

def clean_index(dirname):
  # Always create the index from scratch
  if not os.path.exists(dirname):
      os.mkdir(dirname)
  print(dirname, get_schema())
  ix = index.create_in(dirname, get_schema())
  writer = ix.writer()

  doclist = [u'../IRdocs/test1.txt',u'../IRdocs/test2.txt',u'../IRdocs/test3.txt']
  # Assume we have a function that gathers the filenames of the
  # documents to be indexed
  #for path in my_docs():
  for path in doclist:
    add_doc(writer, path)
    
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

clean_index("newindex")
ix = index.open_dir("newindex")
searcher = ix.searcher()
parser = QueryParser("content", ix.schema)
myquery = parser.parse(u"konijn")
results = searcher.search(myquery)

print(len(results))
print([result for result in results])
searcher.close()