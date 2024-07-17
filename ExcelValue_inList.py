"""
pre requisites
pip install pandas
pip instal openpyxl
"""

import pandas as pd
from tkinter import filedialog

ControlList=["User1@domain.com", "User2@domain.com"]
StartDir = r"C:\Users\vicferre\Documents"
end = filedialog.askopenfilename(initialdir=StartDir)
Arq = pd.read_excel(end)
print (type(Arq))
print (Arq['ColunmName'])

for value in Arq['ColunmName']:
    if value in ControlList:
        print (value, "is present in the file")
    else:
        print(value,"doesn't exist in file")