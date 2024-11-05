#no dependencies required for the code
import xml.etree.ElementTree as ET
from tkinter import filedialog
global root

while True:
    print ("\n type 1 do create XML root")
    print("type 2 to add new subelement in tree")
    print("type 3 to save the xml file")
    print(" type 9 to print current XML")
    opc = input("\n digite opção: ")

    if opc=="1":
        roottg = input("Inform the tag name to be used as root:    ")
        root = ET.Element(roottg)
    if opc=="2":
        #PEL = input("Type parent element name:  ")
        NElement = input("type child element tag:   ")
        #ParentEl = ".//"+PEL
        #print(ParentEl)
        Nel = ET.SubElement(root,NElement)
        while True:
            AtrKey = input("Inform the key of the atribute, if the value is 'quit' will quit atr conf: ")
            if AtrKey == "quit":
                break
            AtrVl = input("type atribute value: ")
            Nel.set(AtrKey,AtrVl)
        txt = input("type node text: ")
        Nel.text=txt
    if opc=="3":
        tree = ET.ElementTree(root)
        path = filedialog.asksaveasfilename(initialdir="Documents")
        print(path)
        tree.write(path)
    if opc =="9":
        print(root, "\n  bytes")
        print(ET.tostring(root))

    if opc == "q": 
        break
