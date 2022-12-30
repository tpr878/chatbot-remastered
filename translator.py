import translators as ts

def hin_to_eng(word):
    in_english=ts.google(word, from_language='hi', to_language='en')
    return in_english

def eng_to_hin(word):
    in_hindi=ts.google(word, from_language='en', to_language='hi')
    return in_hindi

# print(hin_to_eng('जिजीविषा'))

