import xml.etree.ElementTree as ET

import re


folder_name="training_data"
catchphrases=[]
sentences=[]
generated_catchphrases=[]





def get_catchphrases(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    return [l.text for l in root.find('catchphrases').findall('catchphrase') ]

def get_sentence(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    return str(root.find('sentences').text)

def getall_sentences(string):
    return string.split(".\n")

def NaturalLanguageProcessing(title,string):
    """
    Write the code for NLP stuff here
    :return: return array list
    """
    print ("In NLP , Title :",title)

    sentences=getall_sentences(string)

    return []

def get_title(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    #print (root.find('name').text)
    return str(root.find('name').text)
    #return str(root.find('sentences').text)


def fix_xml(filename):
    #Read file and save it back in temp folder
    pattern=re.compile(".*\"id=c[0-9]*\".*")
    with open(filename) as text_file:
        newlines =[ line.replace("\"id=c","id=\"c")  if pattern.match(line) else line  for line in text_file]
    #Write to File
    with open(filename, 'w') as f:
        for s in newlines:
            f.write(s)

def roc(filename):
    """
    Call ROC for each XML file to do 3 things
    1. Parse Sentences stored in sentences list
    2. Parse Catch phrases as list in  catchphrases
    3. Run Machine learning algo on top of it and return generated_catchphrases
    """
    print ("For file : " +filename )
    #parser = ET.XMLParser(encoding="utf-8")

    fix_xml(filename)
    catchphrases=get_catchphrases(filename)
    blob=get_sentence(filename)
    #print blob
    generated_catchphrases=NaturalLanguageProcessing(get_title(filename),blob)
    assert type(generated_catchphrases)==list, " Return list from NaturalLanguageProcessing"



    #print "\n".join(catchphrases)


def get_precision(a,g):
    return 0
def get_recall(a,g):
    return 0
def get_ratio_g_a(a,g):
    return 0



def print_results():
    """
    Uses  catchphrases and generated_catchphrases
    Prints Results
    """

    print ("Generated Catchphrases" , generated_catchphrases)

    print ("============Results=============")
    print ("Precision :" , get_precision(catchphrases,generated_catchphrases))
    print ("Recall :" , get_recall(catchphrases,generated_catchphrases))
    print ("Ratio avg(count(generated_catchphrase)): avg(count(actual_catchphrase))- " , get_ratio_g_a(catchphrases,generated_catchphrases))

if __name__=="__main__":
    roc(folder_name+"/"+"06_6.xml")
    print_results()


