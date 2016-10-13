import xml.etree.ElementTree as ET
from xml.parsers import expat


folder_name="training_data"
catchphrases=[]
sentences=[]
generated_catchphrases=[]





def get_catchphrases(filename):
    return []


def get_sentences(filename):
    return []




def roc(filename):
    """
    Call ROC for each XML file to do 3 things
    1. Parse Sentences stored in sentences list
    2. Parse Catch phrases as list in  catchphrases
    3. Run Machine learning algo on top of it and return generated_catchphrases
    """
    print ("For file : " +filename )
    #parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(folder_name+'/'+filename,parser=expat.ParserCreate('ASCII'))




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
    print ("============Results=============")
    print ("Precision :" , get_precision(catchphrases,generated_catchphrases))
    print ("Recall :" , get_recall(catchphrases,generated_catchphrases))
    print ("Ratio avg(count(generated_catchphrase)): avg(count(actual_catchphrase))- " , get_ratio_g_a(catchphrases,generated_catchphrases))

if __name__=="__main__":
    roc("06_6.xml")
    print_results()


