#simulated database with a list of dictionaries
InfoBlock = [
    {'title':'Python programing language','url':'https://www.python.org/'},
    {'title':'python snake','url':'https://en.wikipedia.org/wiki/Pythonidae'},
    {'title':'Javascript','url':'https://developer.mozilla.org/pt-BR/docs/Web/JavaScript'}
    
    ]

def Search_Keyword(Db, Userkey):
    key = Userkey.lower() # key to be searched will be in lower case

    results = [row for row in Db if key in row['title'].lower()] #can return mulriple results in a list, the search will be case insensitive
    return results

while True:
    Srch = input("what do you want to seach? type end to quit: ")
    if Srch == "end":
        break
    found = Search_Keyword(InfoBlock, Srch)
    for row in found:
        print (row)

