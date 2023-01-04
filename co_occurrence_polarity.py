import sqlite3

con = sqlite3.connect('chatbot.db', check_same_thread= False)
cursorObj = con.cursor()

def co_occurrence_polarity(w):

    sql = " SELECT * FROM co_occurrence_words WHERE word = ?"
    word = (w,)
    cursorObj.execute(sql,word)

    myresult = cursorObj.fetchone()

    if myresult == None:
        return None 
    else:
        return myresult[1]
    # return myresult[1]

# print(polarity_finder('यह'))
# print(polarity_finder('मूवी'))
# print(polarity_finder('बदसूरत'))
# print(polarity_finder('नहीं'))
# print(polarity_finder('है'))