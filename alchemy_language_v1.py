import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1
from roc import get_sentence,fix_xml
from nlp import get_summary

alchemy_language = AlchemyLanguageV1(api_key='cc6bafec52746e499a705e0f9d5f51c10758f679');

url = 'https://developer.ibm.com/watson/blog/2015/11/03/price-reduction-for-watson-personality-insights/'

# print(json.dumps(alchemy_language.targeted_sentiment(text='I love cats! Dogs are smelly.',
#                                                      targets=['cats', 'dogs'], language='english'), indent=2))
# print(json.dumps(alchemy_language.targeted_emotion(text='I love apples. I hate bananas',
#                                                    targets=['apples', 'bananas'], language='english'), indent=2))

# print(json.dumps(alchemy_language.author(url=url), indent=2))
# print(json.dumps(alchemy_language.concepts(max_items=2, url=url), indent=2))
# print(json.dumps(alchemy_language.dates(url=url, anchor_date='2016-03-22 00:00:00'), indent=2))
# print(json.dumps(alchemy_language.emotion(url=url), indent=2))
# print(json.dumps(alchemy_language.entities(url=url), indent=2))
# print(json.dumps(alchemy_language.keywords(max_items=5, url=url), indent=2))
# print(json.dumps(alchemy_language.category(url=url), indent=2))
# print(json.dumps(alchemy_language.typed_relations(url=url), indent=2))
# print(json.dumps(alchemy_language.relations(url=url), indent=2))
# print(json.dumps(alchemy_language.language(url=url), indent=2))
# print(json.dumps(alchemy_language.text(url=url), indent=2))
# print(json.dumps(alchemy_language.raw_text(url=url), indent=2))
# print(json.dumps(alchemy_language.title(url=url), indent=2))
# print(json.dumps(alchemy_language.feeds(url=url), indent=2))
# print(json.dumps(alchemy_language.microformats(url='http://microformats.org/wiki/hcard-examples'), indent=2))
# print(json.dumps(alchemy_language.publication_date(url=url), indent=2))
# print(json.dumps(alchemy_language.taxonomy(url=url), indent=2))

output_file = open('output16.json', 'w')

# combined_operations = ['page-image', 'entity', 'keyword', 'title', 'author', 'taxonomy', 'concept', 'doc-emotion']
combined_operations = ['keyword']
filename='training_data/06_16.xml'
fix_xml(filename)
extracted_text=get_sentence(filename)

output_file.write(json.dumps(alchemy_language.combined(extracted_text, extract=combined_operations), indent=2))

output_file.close()

with open('output.json') as data_file:
       data = json.load(data_file)

list_words=[]
for d in data["keywords"]:
   list_words.append(d['text'])

get_summary(extracted_text,list_words)
