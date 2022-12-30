from nltk.sentiment import SentimentIntensityAnalyzer
from translator import eng_to_hin, hin_to_eng 
import sqlite3
import codecs

comparo_list = []
con = sqlite3.connect('chatbot.db')
cursorObj = con.cursor()


with codecs.open('co_occurrence_testfile.txt', encoding='utf-8') as f:
    content = f.read()

print('Data read from file...')

sentences = content.split('। ')

print('Removing unwanted symbols from content...')
for sentence in sentences:
    if '।' in sentence:
        sentence = sentence.replace('।', '')
    elif '\"' in sentence:
        sentence = sentence.replace('\"', '')
    elif '\'' in sentence:
        sentence = sentence.replace('\'', '')
    elif ',' in sentence:
        sentence = sentence.replace(',', '')
      
    words_list = sentence.split()

    for i in range(len(words_list)):
        if words_list[i] != 'sw' and words_list[i-1] != 'sw':
            t = (words_list[i-1], words_list[i])
            comparo_list.append(t)
    

print('Converting tuples into string...')
for i in comparo_list:
    str = ' '
    str = str.join(i)
    comparo_list[comparo_list.index(i)] = str


print('Fetching polarity of co-occurring words...')
for i in comparo_list:
    sia = SentimentIntensityAnalyzer()
    eng_word = hin_to_eng(i)
    polarity = sia.polarity_scores(eng_word).get('compound')
    if polarity != 0.0:
        co_oc_list = []
        print(i, ' --> ', polarity)
        co_oc_list.append(i)
        co_oc_list.append(polarity)
        cursorObj.execute('''INSERT INTO co_occurrence_words(word, polarity) VALUES (?, ?)''', co_oc_list)
        con.commit()
    else:
        print('Word NOT found')
    
print('\nPROCESS COMPLETE')

        