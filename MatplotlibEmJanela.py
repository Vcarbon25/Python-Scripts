from re import X
import tkinter as TK
from matplotlib import pyplot as plt
import numpy as np

raiz = TK.Tk()

##X=np.linspace(0,10,100)
# y=X^3+2*X^2
def desenhar():
    pass
    """'' x=[1,1,1]
    y=[2,5,3]
    print(x,y)
    imagem = plt.plot(x,y)
    Lcurva=TK.Label(raiz,image=imagem,width=300,height=300)
    Lcurva.pack()
    plt.show()"""


Bgrafico = TK.Button(raiz, text="Desenhe", command=desenhar)
Bgrafico.pack()
raiz.mainloop()
