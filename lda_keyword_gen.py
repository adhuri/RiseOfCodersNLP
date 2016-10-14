from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
from roc import get_catchphrases
import os
from roc import get_sentence,fix_xml
from nlp import get_summary
tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

# create sample documents
filename='training_data/06_6.xml'
#fix_xml(filename)
extracted_text=get_sentence(filename)


# list for tokenized documents in loop
texts = []

filename='training_data/06_6.xml'
raw = extracted_text.lower()
tokens = tokenizer.tokenize(raw)



def get_dictionary():
    directory="training_data"
    catch_phrases_str=""
    catch_texts=[]
    catch_tokens=[]
    for filename in os.listdir(directory):
        catch_phrases_str=""
        if filename.endswith(".xml"):
            #fix_xml(directory+"/"+filename)

            catch_phrases=get_catchphrases(directory+"/"+filename)
            for i in catch_phrases:
                catch_phrases_str=catch_phrases_str+i
            catch_tokens=tokenizer.tokenize(catch_phrases_str)
            catch_stopped_tokens = [i for i in catch_tokens if not i in en_stop]
            catch_texts.append(catch_stopped_tokens)
    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(catch_texts)

    #output_file = open('dict.txt', 'w+')
    #output_file.write(dictionary)

    #output_file.close()
    corpus=[dictionary.doc2bow(text) for text in catch_texts]
    return dictionary,corpus

# remove stop words from tokens
stopped_tokens = [i for i in tokens if not i in en_stop]


# add tokens to list
texts.append(stopped_tokens)

dictionary,corpus=get_dictionary()

filee=open("dict_out.txt","w")
filee.write(str(dictionary))
# convert tokenized documents into a document-term matrix


# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=100, id2word = dictionary, passes=20,update_every=0)

print(ldamodel.print_topics(num_topics=100,num_words=5))
