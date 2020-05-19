import mysql.connector
from difflib import get_close_matches
conn =''
def db_connection():

    con = mysql.connector.connect(
        user = 'ardit700_student',
        password = 'ardit700_student',
        host = '108.167.140.122',
        database = 'ardit700_pm1database'
    )
    return con

def db_query(flg,word=''):

    cursor1 = conn.cursor()
    if flg == 1:
        query = cursor1.execute(f'SELECT * FROM Dictionary WHERE EXPRESSION = "{word}" ')
    else:
        query = cursor1.execute('SELECT DISTINCT EXPRESSION FROM Dictionary ORDER BY EXPRESSION')
    return cursor1.fetchall()

def get_close(word,word_list):
    new_word_lst = []
    for item in word_list:
        new_word_lst.append(item[0])

    get_close_word = get_close_matches(word,new_word_lst)
    return get_close_word

def dictionary_sql(word):
    word = word.lower()
    result = db_query(1, word)  # Sending flag 1 for the Word dictionary values

    if len(result) == 0:
        title_word = word.title()
        result = db_query(1, title_word)
        title_len = len(result)

    if title_len == 0:
        upper_word = word.upper()
        result = db_query(1, upper_word)
        upper_len = len(result)
    if upper_len == 0:
        exp = db_query(0)
        close_word = ','.join(get_close(word, exp))
        yn = input(f'Did you mean the below word/words \n{close_word}. \nEnter the correct word from the above list ')
        if yn != '':
            result = db_query(1, yn)

    return result

def user_input():
    inp = input('Please enter a word ')
    results = dictionary_sql(inp)
    if results:
        for result in results:
            print(result[1])
    else:
        print('Not found')

conn = db_connection()
user_input()