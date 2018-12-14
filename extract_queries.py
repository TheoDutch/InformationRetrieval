# -*- coding: utf-8 -*-

#from bs4 import BeautifulSoup
import re
import pandas as pd
from pathlib import Path


def extract_topics(filepath="./data/testset/topics.txt"):
    # open the file
    filepath = Path(filepath)
    infile = open(filepath,"r").read()
    
    # get all the topic numbers
    number_regex = r"\<num> Number: \d{3}"
    topic_numbers = re.findall(number_regex, infile, re.MULTILINE)
    topic_numbers = [el[-3:] for el in topic_numbers]
    
    # get titles of the topic
    topics = []
    for line in infile.splitlines():
        if line.startswith('<title>'):
            topics.append(line.replace('<title> ', ''))
    
    # get the description
    description_regex = r"<desc> Description:([\s\S]*?)<narr>"
    descriptions = re.findall(description_regex, infile, re.MULTILINE)
    descriptions = [el.strip() for el in descriptions]        
    
    # get narative 
    narrative_regex = r"<narr> Narrative:([\s\S]*?)\</top\>"
    narratives = re.findall(narrative_regex, infile, re.MULTILINE)
    narratives = [el.strip() for el in narratives]        
            
    # convert to pandas df for better overview        
    topic_list = pd.DataFrame(
        {'topic_number': topic_numbers
         ,'title': topics
         ,'descritptions': descriptions
         ,'narratives': narratives
        })
    return topic_list
    
if __name__ == '__main__':
    # this function will automatically extract topics needed for TREC_Robust_2004
    extract_topics()
