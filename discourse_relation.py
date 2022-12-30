#conjunction_list1 for conj_after words
conjunction_list1 = ["और", "व", "तथा", "एवं",        \
    "यदि", "अगर", "तो", "चूंकि ",                      \
    "क्योंकि", "लेकिन", "परन्तु", "मगर", "पर", "फिर भी",  \
    "ताकि", "अथवा", "या", "या तो", "या फिर", "वरना",   \
    "के बजाय",'बावजूद']
#conjunction_list2 for conj_infer or conclusive conjunction    
conjunction_list2=["इसीलिए"] 

def discourse_relation(sentence):
    sentence_in_list=sentence.split()
    
    
    # any func to check the existence of conjunction in sentence
    check1=any(item in sentence_in_list for item in conjunction_list1)
    check2=any(item in sentence_in_list for item in conjunction_list2)
    
    #case1 for conj_after
    if check2:
        for i in sentence_in_list:
          for j in conjunction_list2:
            if(i==j):
              return sentence_in_list[sentence_in_list.index(i)+1: ] 
        
    #case2 for conj_infer          
    elif check1:
        for i in sentence_in_list:
           for j in conjunction_list1:
            if(i==j):
                del sentence_in_list[:sentence_in_list.index(i)+1]
        return sentence_in_list
    else:
        return sentence_in_list

    
# print(discourse_relation("कहने को तो यह दो घंटे की फिल्म है लेकिन यह दो घंटे किसी सजा से कम नहीं है"))
# print(discourse_relation("जो भी कहो कुल मिलाकर ब्रेक के बाद ब्रेक से पिछली ही अच्छी है"))
#print(discourse_relation("वो लड़की बहुत अच्छी है"))
#print(discourse_relation("तुम नहीं आये  इसीलिए मैं भी नहीं गयी।"))
#print(discourse_relation("तुम गलत हो कुल मिलाकर यह अच्छा है।"))
# print(discourse_relation('मैं बदसूरत लड़का हूँ'))