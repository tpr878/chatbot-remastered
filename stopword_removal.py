import codecs

with codecs.open("stopword_list.txt", encoding='utf-8') as f:
 
    stop_words = f.read()
    stop_words_list = stop_words.split()

# string = 'पूरी फ़िल्म इस तरह की नहीं बन पायी कि आम आदमी उसे पूरे समय रुचि से देखे'

def stopword_removal(str):
    list = str.split()
    for i in range (len(list)):
        if list[i] in stop_words_list:
            list[i] = 'sw'
    str = ' ' 
    str = str.join(list)
    return str

# print(stopword_removal(string))