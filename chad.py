def total_polarity(string):
    import intensifiers
    from nltk.sentiment import SentimentIntensityAnalyzer
    from translator import hin_to_eng 
    from discourse_relation import discourse_relation
    from negation import negation
    from polarity_finder import polarity_finder
    from co_occurrence_polarity import co_occurrence_polarity
    from stopword_removal import stopword_removal
    from emotion_finder import emotion_finder


    first_list = string.split()
    # words = "मैं बहुत बदसूरत लड़का हूँ"
    # words = "मैं बदसूरत लड़का पहुंच गई हूँ"
    polarity_after_intensifiers = 0.0
    total_polarity = 0.0
    co_oc_polarity = 0.0
    chad_list = []


    ################################## STOP WORD REMOVAL ########################################
    words = stopword_removal(string)

    ################################## DISCOURSE RELATION ########################################

    discourse_list = discourse_relation(words)
    discourse_str = ' '
    discourse_str = discourse_str.join(discourse_list)


    ################################ NEGATION, INTENSIFIERS AND CO-OCCURRENCE WORDS ###################################

    string_list = discourse_str.split() 
    post_negation_list = negation(discourse_str)
    co_oc_list = []
    final_list = []

    if negation(discourse_str) != False:
        for i in post_negation_list:
            temp_list = [] 
            if polarity_finder(i) == None: 
                sia = SentimentIntensityAnalyzer()
                eng_word = hin_to_eng(i)
                polarity = sia.polarity_scores(eng_word).get('compound')
                if '!' in i:
                    polarity = polarity * -1
                    i = i.replace('!', '')
                    temp_list.append(i)
                    temp_list.append(polarity)
                else:
                    temp_list.append(i)
                    temp_list.append(polarity)
                
                final_list.append(temp_list)
            else:
                polarity = polarity_finder(i)
                temp_list.append(i)
                temp_list.append(polarity)
                final_list.append(temp_list)
        for i in final_list:
            total_polarity = total_polarity + i[1]

        emotion = emotion_finder(post_negation_list)
    else:
        after_intensifiers = intensifiers.intensifiers(discourse_str)

        for i in after_intensifiers:
            if i[0] == "*":
                j = i[1:]
                if polarity_finder(j) == None:
                    sia = SentimentIntensityAnalyzer()
                    eng_word = hin_to_eng(j)
                    polarity_after_intensifiers = polarity_after_intensifiers + (sia.polarity_scores(eng_word).get('compound')*1.5)
                    # after_intensifiers.remove(i)
                    after_intensifiers = list(map(lambda x: x.replace(i, 'N/A'), after_intensifiers))
                else:
                    polarity_after_intensifiers = polarity_after_intensifiers + (polarity_finder(j)*1.5)
                    # after_intensifiers.remove(i) 
                    after_intensifiers = list(map(lambda x: x.replace(i, 'N/A'), after_intensifiers))
        
        for i in after_intensifiers:
            temp_co_oc_list = []
            temp_co_oc_list.append(after_intensifiers[after_intensifiers.index(i)-1])
            temp_co_oc_list.append(i)
            co_oc_list.append(temp_co_oc_list)
            
        co_oc_list.remove(co_oc_list[0])
        co_oc_final_list = []

        for i in co_oc_list:
            co_oc_string = ' '
            co_oc_string = co_oc_string.join(i)
            co_oc_final_list.append(co_oc_string)
        
        for i in co_oc_final_list:
            if co_occurrence_polarity(i) != None:
                co_oc_polarity = co_oc_polarity + co_occurrence_polarity(i)
                split_string = i.split()
                for j in split_string:
                    for k in after_intensifiers:
                        if j == k:
                            after_intensifiers.remove(k)
                            
        for i in after_intensifiers:
            if polarity_finder(i) == None:
                    sia = SentimentIntensityAnalyzer()
                    eng_word = hin_to_eng(i)
                    total_polarity = total_polarity + (sia.polarity_scores(eng_word).get('compound')) + polarity_after_intensifiers
            else:
                total_polarity = total_polarity + (polarity_finder(i)) + co_oc_polarity + polarity_after_intensifiers          

        emotion = emotion_finder(discourse_list)
    
    total_polarity = round((total_polarity/len(first_list)), 3)
    chad_list.append(emotion)
    chad_list.append(total_polarity)

    return chad_list

# test = 'object is not subscriptable'
# print(total_polarity(test))






