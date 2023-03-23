import pandas as pd

testexcel = r"C:\Users\vicferre\Desktop\C.xlsx"
testarq = r"C:\Users\vicferre\Desktop\VIctor Carbón Ferreira Dados PC Oracle\SI.csv"
A=pd.read_csv(testarq)
I=pd.read_excel(testexcel)
print(I)
print(A)
print(type(I))
coluna=I.loc[2] #loc vai selecionar a coluna 2, os indices tem a ordem de 0,1,2...
el=I.iat[1,1] #seleciona um elemento especifico[linha, coluna] os indices começam como 0,1,2...
print(el, type(el))
print(type("s"))