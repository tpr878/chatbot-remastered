import sqlite3
from chad import total_polarity

con = sqlite3.connect('test_chatbot.db')
cursorObj = con.cursor()


joy_list = ['उत्साह', 'आनंद', 'ख़ुश', 'ख़ुशी', 'प्रसन्न', 'प्रसन्नता', 'संतुष्टि', 'सफ़लता', 'सफ़ल', 'अच्छा', 'ठीक', 'बढ़िया']
trust_list = ['आशा', 'भरोसा', 'विश्वास', 'यक़ीन', 'स्वीकार', 'प्रशंसा', 'प्रशस्ति', 'इज़्ज़त', 'सम्मान', 'मान']
fear_list = ['आशंका', 'चिंता', 'डर', 'भय', 'परेशान', 'परेशानी', 'बेचैनी', 'झिझक', 'ख़ौफ़', 'ख़तरा', 'घबराहट', 'चौंकना', 'चौकाने']
surprise_list = ['आश्चर्य', 'हैरत', 'अचरज', 'अनोखा', 'अचंभा', 'आश्चर्यजनक', 'ताज्जुब', 'विस्मय']
sadness_list = ['बुरी', 'बुरा', 'दुखी', 'दु:खी', 'दुख', 'दु:ख', 'उदास', 'अशुभ', 'गंभीर', 'रूखा', 'रूखे', 'फीका', 'फीके', 'शोक']
disgust_list = ['घृणा', 'क्लांति', 'ऊब', 'ऊबना', 'असंतोष', 'जुगुप्सा', 'विरक्ति', 'चिढ़', 'नफ़रत', 'निंदा']
anger_list = ['हंगामा', 'गुस्सा', 'क्रोध', 'नाराज़', 'नाराज़गी', 'खुन्नस', 'कोप', 'प्रकोप', 'चिड़चिड़ा', 'क्रुद्ध', 'क्रोधित']
interest_list = ['रुचि', 'प्रत्याशा', 'जागरूकता', 'इच्छा', 'अभिलाषा', 'दिलचस्पी', 'चाह', 'पसंद', 'मनपसंद', 'अभिरुचि']

emotion_groups = {'joy': joy_list, 'trust': trust_list, 'fear': fear_list, 'surprise': surprise_list, 'sadness': sadness_list, 'disgust': disgust_list, 'anger': anger_list, 'interest': interest_list}

emotions = list(emotion_groups.keys())
lists = list(emotion_groups.values())


# cursorObj.execute('''CREATE TABLE  emotion_groups (word TEXT, emotion TEXT, polarity REAL, intensity INTEGER)''')
# con.commit()

    
for emotion in emotion_groups:
    for word in emotion_groups.get(emotion):
        cursorObj.execute('''SELECT * FROM emotion_groups WHERE word = "{}" '''.format(word))
        myresult = cursorObj.fetchone()
        
        if myresult == None:
            input_list = []
            polarity = total_polarity(word)[1]

            input_list.append(word)
            input_list.append(emotion)
            input_list.append(polarity)
            print(word, '-->', emotion, '-->', polarity)
            cursorObj.execute('''INSERT INTO emotion_groups(word, emotion, polarity) VALUES (?, ?, ?)''', input_list)

for emotion in emotion_groups:
    for word in emotion_groups.get(emotion):
        
        cursorObj.execute('''SELECT MAX(polarity) FROM emotion_groups WHERE emotion = "{}" '''.format(emotion))
        max = cursorObj.fetchone()[0]
        
        if max == 0:
            cursorObj.execute('''SELECT MIN(polarity) FROM emotion_groups WHERE emotion = "{}" '''.format(emotion))
            max = cursorObj.fetchone()[0]

        cursorObj.execute('''SELECT polarity FROM emotion_groups WHERE word = "{}" '''.format(word))
        word_polarity = cursorObj.fetchone()[0]

        intensity = round((word_polarity/max), 3)

        scale = 0
        if intensity >= 0 and intensity < 0.3:
            scale = 1
        elif intensity >= 0.3 and intensity < 0.6:
            scale = 2
        else:
            scale = 3
        
        cursorObj.execute('''UPDATE emotion_groups SET intensity = {}, scale = {} WHERE word = "{}" '''.format(intensity, scale, word))


        con.commit()




# print('TABLE UPDATED')


