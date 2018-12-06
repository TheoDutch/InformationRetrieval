# -*- coding: utf-8 -*-

#from bs4 import BeautifulSoup
import re
import pandas as pd

# open the file
infile = open("./data/testset/topics","r").read()

# get all the topic numbers
number_regex = r"\<num> Number: \d{3}"
topic_numbers = re.findall(number_regex, infile, re.MULTILINE)
topic_numbers = [el[-3:] for el in topic_numbers]

# get titles of the topic
topics = []
for line in infile.splitlines():
    if line.startswith('<title>'):
        topics.append(line.replace('<title> ', ''))

# get the description <- somehow hot working
#description_regex = r"<desc> Description:([\s\S]*?)<narr>"
#descriptions = re.findall(description_regex, infile, re.MULTILINE)
#descriptions = [el.strip() for el in descriptions]        

# get narative <- somehow not working
#narrative_regex = r"<narr> Narrative:([\s\S]*?)\</top\>"
#narratives = re.findall(narrative_regex, infile, re.MULTILINE)
#narratives = [el.strip() for el in narratives]        
        
# convert to pandas df for better overview        
topic_list = pd.DataFrame(
    {'topic_number': topic_numbers
     ,'title': topics
     #,'descritptions': descriptions
     #,'narratives': narratives
    })