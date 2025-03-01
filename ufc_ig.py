# -*- coding: utf-8 -*-
"""UFC_IG.ipynb

pip install nltk

pip install spacy

pip install stopwordsiso

#import nlp tools
import nltk
import stopwordsiso as stops
from string import punctuation
import spacy

#import tools for visualization and analysis
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from wordcloud import WordCloud

##Data manipulation with Pandas

# Load your data from IG
df = pd.read_json("path/data.json")

#Explore your DF:

df.head(10)

#Exemple of manipulation 1: ordering by most comments
df_sorted = df.sort_values(by='commentsCount', ascending=False)

#Exemple of manipulation 2: selecting n posts with most comments
df_mostcomments = df_sorted.head(n)

# Grouping all posts by IG user: merging values in 'caption' column for the same user in a dictionary

grouped_text = df_mostcomments.groupby('inputUrl')['caption'].apply(lambda x: ' '.join(x)).to_dict()

##Cleaning the text with NLTK

#Establishing stopwords, punctuation marks, and common terms

stops_en = stops.stopwords('en')
stops_pt = stops.stopwords('pt')
punctuation_marks = {'.', ',', '!', '?', ';', ':', '-', '_', '(', ')', '[', ']', '{', '}',
    '"', "'", '<', '>', '/', '\\', '@', '#', '$', '%', '^', '&', '*',
    '+', '=', '|', '~', '`', '…', '“', '”', '‘', '’', '•', '¶', '©', '®'}
stops_ufc = {'stylebender', 'israeladesanya', 'mma', 'israel', 'adesanya', 'thenotoriousmma', 'conor', 'mcgregor', 'conormcgregor', 'charlesdobronx', 'oliveira', 'charlesdobronxs','charles', 'dobronx', 'francisngannou', 'francis', 'ngannou', 'jonny', 'bones', 'jonnybones', 'ufc'}

# Generate and export txt files for each user

from google.colab import files

import os

for user, text in grouped_text.items():
    # Extract the username from the URL
    username = user.rstrip("/")
    username = username.split('/')[-1]
    #normalize text
    text = text.lower()
    normalized_no_stops = [word for word in text.split() if word not in stops_en and word not in stops_pt and word not in stops_ufc]
    normalized_no_stops_text = ''.join(normalized_no_stops)
    normalized = ''.join([char for char in text if char not in punctuation and char.isnumeric()==False])
    normalized = [word for word in normalized.split() if word not in stops_en and word not in stops_pt and word not in stops_ufc]
    normalized = ' '.join(normalized)

    # Create a filename using the extracted username
    filename = f"{username}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(normalized)
        files.download(filename)





