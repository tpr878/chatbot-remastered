import sqlite3

con = sqlite3.connect('chatbot.db')
cursorObj = con.cursor()

def polarity_finder(w):

    sql = " SELECT * FROM chatbot WHERE word = ?"
    word = (w,)
    cursorObj.execute(sql,word)

    myresult = cursorObj.fetchone()

    if myresult == None:
        return False
    else:
        return myresult[1]


polarity_finder("भूल")
