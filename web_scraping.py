import requests
from bs4 import BeautifulSoup
from nltk.sentiment import SentimentIntensityAnalyzer
from translator import eng_to_hin, hin_to_eng 
import sqlite3

# dbms connection
con = sqlite3.connect('chatbot.db')
cursorObj = con.cursor()
cursorObj.execute("CREATE TABLE chatbot(word text, polarity real)")
print ("Chatbot Table created successfully")
# cursorObj.execute("CREATE TABLE negative(word text, polarity real)")
# print ("Negative Table created successfully")
# cursorObj.execute("CREATE TABLE neutral(word text, polarity real)")
# print ("Neutral Table created successfully")
con.commit()


# 'https://www.hindikiduniya.com/essay/essay-on-disadvantages-of-internet-in-hindi/'
# 'https://www.deepawali.co.in/aarakshan-ki-samasya-essay-hindi.html'
url_list = ['https://hindi.webdunia.com/hindi-essay/essay-on-lockdown-120051900052_1.html']

for url in url_list:
    r = requests.get(url)
    htmlContent = r.content

    soup = BeautifulSoup(htmlContent, 'html.parser')

    text = soup.get_text()
    l = text.split() # all website content
    l2 = [] # all hindi content from the website
    list = [] # final list

    for element in l:
        # devnagiri unicode : \u0900 to \u0963 and \u0972 to \u097f
        if '\u0900' <= element <= '\u0963' or '\u0972' <= element <= '\u097f':
            l2.append(element)

    print('Creating sublists with hindi words and their respective polarities...')
    for word in l2:
        temp_list = [] # for sublists 
        sia = SentimentIntensityAnalyzer()
        eng_word = hin_to_eng(word)
        polarity = sia.polarity_scores(eng_word).get('compound')
        temp_list.append(word)
        temp_list.append(polarity)

        
        cursorObj.execute('''INSERT INTO chatbot(word, polarity) VALUES (?, ?)''', temp_list)
        
        con.commit()
        
        list.append(temp_list)
        print(temp_list)
        
    print('\nURL: ', url, '\nDATA STORED IN DATABASE SUCCESSFULLY\n')






