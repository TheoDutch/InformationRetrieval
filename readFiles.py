# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 11:58:38 2018

@author: kstoutjesdijk
"""

#werkt als er 1 doc is
#==============================================================================
# from bs4 import BeautifulSoup
# infile = open("test","r")
# contents = infile.read()
# soup = BeautifulSoup(contents, 'xml')
# titles = soup.find_all('TEXT')
# for title in titles:
#     #print(title.get_text())
#     pass
#==============================================================================

from bs4 import BeautifulSoup

infile = open("test2","r").read()

infile = '<root>'+infile+'</root>'

soup = BeautifulSoup(infile, 'xml')
docid  = soup.find_all('DOCID')
for id in docid:
    print(id.get_text())
texts = soup.find_all('TEXT')
for text in texts:
    print(text.get_text())
    
