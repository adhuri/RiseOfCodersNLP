import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1
from roc import get_sentence,fix_xml,get_title
from nlp import get_summary
import os
import os.path
import codecs

def generate_keywords_dict():
    global keywords_dict
    alchemy_language = AlchemyLanguageV1(api_key='c967d6e7e3bb22b82ea026dfabb30af595729d75');

    url = 'https://developer.ibm.com/watson/blog/2015/11/03/price-reduction-for-watson-personality-insights/'
    output_file = open('output.json', 'w')

    # combined_operations = ['page-image', 'entity', 'keyword', 'title', 'author', 'taxonomy', 'concept', 'doc-emotion']
    combined_operations = ['keyword']

    #fix_xml(filename)

    list_words=[]
    directory='training_data'
    list_file=open('list_file.txt',"a")
    title=""
    for filename in os.listdir(directory):
        json_filename='json/'+filename+'.json'
        filename=directory+"/"+filename
        temp_list_keys=[]

        keywords_dict={}

        os.remove('output.json')
        output_file = open('output.json', 'w')


        if filename.endswith(".xml"):
            fix_xml(filename)
            title=get_title(filename)
            print filename
            extracted_text=get_sentence(filename)
            try:
                if(not os.path.isfile(json_filename)):

                    output_file.write(json.dumps(alchemy_language.combined(extracted_text, extract=combined_operations), indent=2))
                    output_file.close()
                    with open('output.json') as data_file:
                        data = json.load(data_file)
                else:
                    with open(json_filename) as data_file:
                        #data_file1=json.dumps(data_file)
                        data = json.load((data_file))

                for d in data["keywords"]:
                    temp_list_keys.append(d['text'])
                    list_words.append(d['text'])
                    list_file.write(" " + str(d['text']))
                    list_file.flush()
            except Exception as e:
                print e

            json_file=open(json_filename,'w')
            keywords_dict.update({"filename":filename,"casename":title,"keywords":temp_list_keys})
            keywords_str=json.dumps(keywords_dict)
            keywords_json=json.loads(keywords_str)
            json_file.write(str(keywords_json))
            json_file.close()
    list_file.close()


generate_keywords_dict()
filename='training_data/06_9.xml'
#get_summary(extracted_text,list_words)
