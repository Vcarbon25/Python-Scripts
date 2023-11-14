import tkinter as TK
from tkinter import filedialog
import xml.etree.ElementTree as ET
from lxml import etree
root=TK.Tk()
root.config(background="Blue")
LbFile = TK.Label(root,text="fileName")
LbFile.grid(row=0,column=0)
BOpenFile=TK.Button(root,text="Choose File")
BOpenFile.grid(row=1,column=0)
RootList=["Default"]

LstNodes=[]
LBNodes=TK.Listbox(root,listvariable= LstNodes)
LBNodes.grid(row=3,column=0)
LbContent=TK.LabelFrame(root,text="Atributos",width=300,height=500,background="gray")
LbContent.grid(row=1,column=1,rowspan=3,padx=5)
FileN=''

def show_atr (window, atr_name, atr_tags=[],atr_vls=[]):
  print(atr_name, atr_tags,atr_vls)
  for element in window.winfo_children():
      element.destroy()
  ScrollCnt = TK.Scrollbar(window)
  ScrollCnt.pack(side="right", fill="y")
  atr_cont=TK.LabelFrame(window, text=atr_name)
  atr_cont.pack()
  for i in range(0,len(atr_tags)):
    atr_sub_name = TK.Text(atr_cont, width=10, height=1)
    atr_sub_name.grid(row=i,column=0)
    atr_sub_name.insert("1.0",str(atr_tags[i]))
    atr_conec=TK.Label(atr_cont, text="-->")
    atr_conec.grid(row=i,column=1)
    atr_vl = TK.Text(atr_cont,width=20, height=3)
    atr_vl.grid(row=i,column=2)
    atr_vl.insert("1.0",str(atr_vls[i]))

def SelectionChanged(a):
    lista = LBNodes
    index = int(lista.curselection()[0])
    global FileN
    tree = ET.parse(FileN)
    root=tree.getroot()
    NodeCont=dict(root[index].attrib)
    chs=list(NodeCont.keys())
    vls=list(NodeCont.values())
    txt =[str(root[index].tag)]
    for i in range(0,len(chs)-1):
        txt.append("\n\t"+chs[i]+" : "+vls[i])
    print(NodeCont)
    Nodetg=root[index].tag
    # temp = etree.tostring(str(NodeCont),pretty_print=True,encoding=str)
    #lbtext=Nodetg+"\n"+temp
    show_atr(LbContent, Nodetg,chs,vls)
    #LbContent.config(text=txt,anchor="w",justify=TK.LEFT)
LBNodes.bind("<<ListboxSelect>>",SelectionChanged)

def XmlParser(FileN):
    tree=ET.parse(FileN)
    global RootList
    RootList
    RootList[0]=tree.getroot().tag
    #CbRoots.config(*RootList)
    LstNodes=[]
    for child in tree.getroot():
        LstNodes.append(child.tag)
    LBNodes.insert(0,*LstNodes)
    
    
    #CbRoots.config(RootList)
def Open_File():
    LBNodes.delete(0,TK.END)
    global FileN
    FileN=filedialog.askopenfilename()
    Name=FileN.split('/')
    LbFile.config(text=str(Name[-1]))
    FileExt=Name[-1].split('.')[-1] #gets the file extension, character after the dot
    if FileExt=='xml':
        XmlParser(FileN)
BOpenFile.config(command=Open_File)
root.mainloop()