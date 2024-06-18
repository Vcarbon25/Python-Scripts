"""
requirements
pip install tkinterPDFViewer
"""
from tkinterPdfViewer import tkinterPdfViewer as pdf
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()

v1 = pdf.ShowPdf()
arq=filedialog.askopenfilename()
v2 = v1.pdf_view(root, pdf_location=arq, width=100, height=77, dpi=100)
v2.pack()

root.mainloop()