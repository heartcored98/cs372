import pandas as pd
import kss
from tqdm import tqdm

df = pd.read_csv('../data/raw_wiki_ko.txt', header=None, delimiter='\t') 
sent_list = list()

for i, row in tqdm(enumerate(df.iterrows())):
    """
    Ref : https://github.com/likejazz/korean-sentence-splitter
    """
    paragraph = str(row[1].values[0])
    sents = kss.split_sentences(paragraph)
    for j, sent in enumerate(sents):
        sent_list.append(sent)

with open('../data/raw_wiki_ko_sent.txt', 'w', encoding='utf-8') as output:
    for sent in tqdm(sent_list):
        output.write(sent)
        output.write('\n')