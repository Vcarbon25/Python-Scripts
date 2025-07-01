import threading
from datetime import datetime
def funcao_1():
    for i in range(0,50):
        print('first function ',i)

def funcao_2():
    for x in range(0,50):
        print('second function',x)

'''

#like this functions are called sequentialy
start = datetime.now()
funcao_1()
funcao_2()
end=datetime.now()

'''
#now the functions are still being executed by the same interpreter, but it's focus is divided in two tasks
threading.Thread(target=funcao_1).start()
threading.Thread(target=funcao_2).start()


