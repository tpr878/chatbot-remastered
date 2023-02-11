import sqlite3

def emotion_finder(list):
    con = sqlite3.connect('chatbot.db', check_same_thread = False)
    cursorObj = con.cursor()
    counter_dict = {'joy': 0, 'trust': 0, 'fear': 0, 'surprise': 0, 'sadness': 0, 'disgust': 0, 'anger': 0, 'interest': 0}
    score_dict = {'joy': 0, 'trust': 0, 'fear': 0, 'surprise': 0, 'sadness': 0, 'disgust': 0, 'anger': 0, 'interest': 0}
    
    joy_counter = 0
    joy_score = 0

    trust_counter = 0
    trust_score = 0

    fear_counter = 0
    fear_score = 0
    
    surprise_counter = 0
    surprise_score = 0
    
    sadness_counter = 0
    sadness_score = 0
    
    disgust_counter = 0
    disgust_score = 0
    
    anger_counter = 0
    anger_score = 0
    
    interest_counter = 0
    interest_score = 0


    for word in list:
        if '।' in word:
            word2 = word.replace('।', '')
            list[list.index(word)] = word2
        
        if ',' in word:
            word2 = word.replace(',', '')
            list[list.index(word)] = word2

    for word in list:
        sql = "SELECT * FROM emotion_groups WHERE word = ?"
        w = (word,)
        cursorObj.execute(sql, w)

        myresult = cursorObj.fetchone()
        
        if myresult == None:
            # not_found_counter += 1
            pass
        
        elif myresult[1] == 'joy':
            joy_counter += 1
            joy_score += myresult[4]
            counter_dict.update({'joy':joy_counter})
            score_dict.update({'joy':joy_score})
        
        elif myresult[1] == 'trust':
            trust_counter += 1
            trust_score += myresult[4]
            counter_dict.update({'trust':trust_counter})
            score_dict.update({'trust':trust_score})
       
        elif myresult[1] == 'fear':
            fear_counter += 1
            fear_score += myresult[4]
            counter_dict.update({'fear':fear_counter})
            score_dict.update({'fear':fear_score})
       
        elif myresult[1] == 'surprise':
            surprise_counter += 1
            surprise_score += myresult[4]
            counter_dict.update({'surprise':surprise_counter})
            score_dict.update({'surprise':surprise_score})
        
        elif myresult[1] == 'sadness':
            sadness_counter += 1
            sadness_score += myresult[4]
            counter_dict.update({'sadness':sadness_counter})
            score_dict.update({'sadness':sadness_score})
        
        elif myresult[1] == 'disgust':
            disgust_counter += 1
            disgust_score += myresult[4]
            counter_dict.update({'disgust':disgust_counter})
            score_dict.update({'disgust':disgust_score})
        
        elif myresult[1] == 'anger':
            anger_counter += 1
            anger_score += myresult[4]
            counter_dict.update({'anger':anger_counter})
            score_dict.update({'anger':anger_score})
        
        elif myresult[1] == 'interest':
            interest_counter += 1
            interest_score += myresult[4]
            counter_dict.update({'interest':interest_counter})
            score_dict.update({'interest':interest_score})

    
    max_emotion = max(zip(score_dict.values(), score_dict.keys()))[1]  
    max_counter = counter_dict.get(max_emotion)
    max_score = score_dict.get(max_emotion)

    if max_counter == 0:
        return None 

    avg_emotion_scale = round((max_score/max_counter), 3)
    final_list = []
    final_list.append(max_emotion)
    final_list.append(avg_emotion_scale)


    return final_list

# test = 'object is not subscriptable'
# testlist = test.split()
# print(emotion_finder(testlist))