import sqlite3

# dbms connection
con = sqlite3.connect('chatbot.db')
cursorObj = con.cursor()
# cursorObj.execute("CREATE TABLE positive(word text, polarity real)")
# print ("Positive Table created successfully")
# cursorObj.execute("CREATE TABLE negative(word text, polarity real)")
# print ("Negative Table created successfully")
# cursorObj.execute("CREATE TABLE neutral(word text, polarity real)")
# print ("Neutral Table created successfully")

# con.commit()

word="word"
polarity = 1.0
entities = (word, polarity)

# depending upon polarity being +ve, -ve, or neutral, adding each word to its respective dictionary
if polarity > 0:
    cursorObj.execute('''INSERT INTO positive(word, polarity) VALUES (?, ?)''', entities)
elif polarity < 0:
    cursorObj.execute('''INSERT INTO negative(word, polarity) VALUES (?, ?)''', entities)
else:
    cursorObj.execute('''INSERT INTO neutral(word, polarity) VALUES (?, ?)''', entities)
con.commit()