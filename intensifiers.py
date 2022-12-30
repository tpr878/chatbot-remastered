intensifiers_list = ["बिल्कुल", "अत्यधिक", "बहुत"]

def intensifiers(input):
    word_list = input.split()
    for i in range(len(intensifiers_list)):
        for j in range(len(word_list)):
                if intensifiers_list[i] == word_list[j]:
                    word_list[j+1] = "*" + word_list[j+1]
    
    if("बहुत" in word_list):
        word_list.remove("बहुत")
        # print(word_list)
    
    if("बिल्कुल" in word_list):
        word_list.remove("बिल्कुल")
        # print(word_list)
    
    if("अत्यधिक" in word_list):
        word_list.remove("अत्यधिक")
        # print(word_list)

    return word_list
