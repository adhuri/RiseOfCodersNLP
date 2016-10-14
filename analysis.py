import json
import difflib
#import nltk
tolerance=0.6
with open('9.json') as data_file:    
    data1 = json.load(data_file)

with open('16.json') as data_file:    
    data2 = json.load(data_file) 

def similar(w1, w2):
   w1 = w1 + ' ' * (len(w2) - len(w1))
   w2 = w2 + ' ' * (len(w1) - len(w2))
   return sum(1 if i == j else 0 for i, j in zip(w1, w2)) / float(len(w1))   

for i in data1['keywords']:
	for j in data2['keywords']:
		d = difflib.SequenceMatcher(None, i, j).ratio()
		#d = similar(i, j);
		#text = nltk.Text(i.lower() for i in nltk.corpus.brown.words())
		#d = text.similar(j);
		if(d > tolerance):
			print ("%10s | %10s | %3.2f "%(i,j,d))
