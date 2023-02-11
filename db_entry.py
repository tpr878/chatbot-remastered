from nltk.sentiment import SentimentIntensityAnalyzer
import sqlite3
from translator import eng_to_hin, hin_to_eng 

con = sqlite3.connect('chatbot.db')
cursorObj = con.cursor()

db_string = 'मैं बहुत अच्छा महसूस कर रही हूँ लेकिन मेरे जीवन में एक समस्या है मेरा शारीरिक स्वास्थ बिलकुल ठीक है मेरा मानसिक स्वास्थ अच्छा नहीं है मेरे साथ एक लड़के ने बुरी तरह से बदतमीज़ी करी नहीं समाप्त'
db_list = db_string.split()

for word in db_list:
    temp_list = [] # for sublists 
    sia = SentimentIntensityAnalyzer()
    eng_word = hin_to_eng(word)
    polarity = sia.polarity_scores(eng_word).get('compound')
    temp_list.append(word)
    temp_list.append(polarity)

    
    cursorObj.execute('''INSERT INTO chatbot(word, polarity) VALUES (?, ?)''', temp_list)
    
    con.commit()

        
print('\nDATA STORED IN DATABASE SUCCESSFULLY\n')
