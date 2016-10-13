


# Method that runs through all sentences and checks the number of keywords present in that sentences
def get_summary(text,list_keywords):
    summary=""
    list_sentences=getall_sentences(text)
    count=0
    for each sentence in list_sentences:
        for each keyword in list_keywords:
            if keyword in sentence:
                count+=1
                if count>1:
                    count=0
                    summary=summary+sentence
                    break


    return summary
