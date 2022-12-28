import sqlite3
import requests
from bs4 import BeautifulSoup
from translator import eng_to_hin, hin_to_eng 
import json
# dbms connection
con = sqlite3.connect('chatbot.db')
cursorObj = con.cursor()
#sql query to get all the data
fetch_chatbot_sql = '''
SELECT * FROM chatbot
'''
#executing the sql query
cursorObj.execute(fetch_chatbot_sql)
#storing the data in a variable using fetchall() method
words=cursorObj.fetchall() # a list of tuples
dict_words=dict(words)
#presenting the data
#print(dict_words)
for i , j  in dict_words.items(): 
    eng_word = hin_to_eng(i)  
    #print(eng_word)
    api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(eng_word)
    response = requests.get(api_url, headers={'X-Api-Key': 'xgCnBVIqBPJa5D9C0PFJHw==GCGiHFsbH3vJqxFy'})
    if response.status_code == requests.codes.ok:
            syn_ant=response.text  # a list of tuples
            res = json.loads(syn_ant) # dictionary
            
            for k , l in res.items():
                if k=="synonyms":
                    for m in l:
                        temp_list1=[] #for sub_lists for synonyms
                        hin_word=eng_to_hin(m)
                        # devnagiri unicode : \u0900 to \u0963 and \u0972 to \u097f
                        if '\u0900' <= hin_word <= '\u0963' or '\u0972' <= hin_word <= '\u097f':
                            temp_list1.append(hin_word)
                            temp_list1.append(j)
                            cursorObj.execute('''INSERT INTO chatbot(word, polarity) VALUES (?, ?)''', temp_list1)
                            print("iteration completed for synonyms")
                            con.commit()      
                elif k=="antonyms":
                    for m in l:
                        temp_list2=[]# for sub_lists for antonyms
                        hin_word=eng_to_hin(m)
                        # devnagiri unicode : \u0900 to \u0963 and \u0972 to \u097f
                        if '\u0900' <= hin_word <= '\u0963' or '\u0972' <= hin_word <= '\u097f':
                            temp_list2.append(hin_word)
                            temp_list2.append(j*(-1))
                            cursorObj.execute('''INSERT INTO chatbot(word, polarity) VALUES (?, ?)''', temp_list2)
                            print("iteration completed for antonyms")
                            con.commit()           
    else:
        print("Error:", response.status_code, response.text)
       
