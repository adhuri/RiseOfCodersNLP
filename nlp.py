
from roc import getall_sentences

# Method that runs through all sentences and checks the number of keywords present in that sentences
def get_summary(text,list_keywords):
    acc_threshold=0.4;
    summary=[]
    list_sentences=[]
    list_sentences=getall_sentences(text)
    count_matched=0.0
    for sentence in list_sentences:
        count_matched=0.0
        for keyword in list_keywords:
            if keyword in sentence:
                count_matched+=len(keyword.split())
                if count_matched/len(sentence.split())>acc_threshold:
                    count_matched=0
                    summary.append(sentence)
                    break


    print "Number of sentences is "+ str(len(summary))
    for i in summary:
        print i
        print "\n"
    return summary
