from translator import eng_to_hin, hin_to_eng 
from negation import negation 
from nltk.sentiment import SentimentIntensityAnalyzer


string = 'यह मूवी अच्छी नहीं है'
string_list = string.split()
post_negation_list = negation(string)
final_list = []

for i in post_negation_list:
    temp_list = [] # for sublists 
    sia = SentimentIntensityAnalyzer()
    eng_word = hin_to_eng(i)
    polarity = sia.polarity_scores(eng_word).get('compound')
    if '!' in i and polarity != 0:
        i = i.replace('!', '')
        polarity = polarity * -1
        temp_list.append(i)
        temp_list.append(polarity)
    else:
        temp_list.append(i)
        temp_list.append(polarity)
    
    final_list.append(temp_list)

print(final_list)


