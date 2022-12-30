import translator
import intensifiers
import polarity_finder
from nltk.sentiment import SentimentIntensityAnalyzer
from translator import eng_to_hin, hin_to_eng 

polarity_after_intensifiers = 0.0
total_polarity = 0.0
words = "मैं बदसूरत लड़का हूँ"


# intensifiers stuff
after_intensifiers = intensifiers.intensifiers(words)

for i in after_intensifiers:
    if i[0] == "*":
        j = i[1:]
        if polarity_finder.polarity_finder(j) == None:
            sia = SentimentIntensityAnalyzer()
            eng_word = hin_to_eng(j)
            polarity_after_intensifiers = polarity_after_intensifiers + (sia.polarity_scores(eng_word).get('compound')*2)
            after_intensifiers.remove(i)
        else:
            polarity_after_intensifiers = polarity_after_intensifiers + (polarity_finder.polarity_finder(j)*2)
            after_intensifiers.remove(i) 

for i in after_intensifiers:
    if polarity_finder.polarity_finder(i) == None:
            sia = SentimentIntensityAnalyzer()
            eng_word = hin_to_eng(i)
            total_polarity = total_polarity + (sia.polarity_scores(eng_word).get('compound'))
            
    else:
        total_polarity = total_polarity + (polarity_finder.polarity_finder(i))
        

total_polarity = total_polarity + polarity_after_intensifiers
print(total_polarity)
print(after_intensifiers)