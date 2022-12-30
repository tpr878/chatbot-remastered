# devnagiri unicode : \u0900 to \u0963 and \u0972 to \u097f

def negation(string):
    neg_count = 0
    conj_count = 0
    conj_list = ['और', 'कि', 'लेकिन', 'पर', 'मगर', 'चाहे', 'या', 'तो', 'क्योंकि', 'जब कि', 'एवं', 'इसलिए', 'या फिर', 'नहीं तो', 'जैसे कि']
    neg_list = ['नहीं', 'न', 'नदारद']
    # example_string = 'यह मूवी अच्छी नहीं है'
    # example_string = 'पूरी फ़िल्म इस तरह की नहीं बन पायी कि आम आदमी उसे पूरे समय रुचि से देखे'
    # example_string = 'न कहानी ढंग की है, न ही पटकथा और न ही निर्देशन'
                    
                    
                    
    string_list = string.split()

    for i in neg_list:
        for j in string_list:
            if i == j:
                neg_count += 1
                # print(i, ' --> negative count = ', neg_count)

    for i in conj_list:
        for j in string_list:
            if i == j:
                conj_count += 1
                # print(i, ' --> conjunction count = ', conj_count)

    
    
    
    # case 1: if sentence has only one negative word
    # example_string = 'यह मूवी अच्छी नहीं है'
    if neg_count >= 1 and conj_count == 0:
        for i in neg_list:
            if i in string_list:
                for j in range(string_list.index(i)):
                    string_list[j]  = '!' + string_list[j]
        
        for i in neg_list:
            for j in string_list:
                if i == j:
                    string_list.remove(j)
        return string_list
    # case 2: if index of conjunction is greater than that of negative word    
    # example_string = 'पूरी फ़िल्म इस तरह की नहीं बन पायी कि आम आदमी उसे पूरे समय रुचि से देखे'
    elif neg_count == 1 and conj_count == 1:
        for i in conj_list:
            for j in neg_list:
                if i in string_list and j in string_list and string_list.index(i) > string_list.index(j):
                    for j in range(string_list.index(i) + 1, len(string_list)):
                        string_list[j]  = '!' + string_list[j]
        for i in neg_list:
            for j in string_list:
                if i == j:
                    string_list.remove(j)
        return string_list
    # case 3: if sentence has 'न' multiple times, separated by commas 
    # example_string = 'न कहानी ढंग की है, न ही पटकथा और न ही निर्देशन'
    elif neg_count > 1 and conj_count >= 1:
        for i in range(len(string_list)):
            if '!' in string_list[i]:
                string_list[i] = string_list[i][1:]
            if string_list[i] in neg_list or string_list[i] in conj_list:
                string_list[i] = string_list[i]
            else:
                string_list[i] = '!' + string_list[i]
        for i in neg_list:
            for j in string_list:
                if i == j:
                    string_list.remove(j)
        return string_list
    else:
        return False 
                   
# print(negation('यह मूवी अच्छी नहीं है'))
# print(negation('पूरी फ़िल्म इस तरह की नहीं बन पायी कि आम आदमी उसे पूरे समय रुचि से देखे'))
# print(negation('न कहानी ढंग की है, न ही पटकथा और न ही निर्देशन'))







