import tkinter as tk

def clicked():
    print("clicked the button")
self = tk.Tk()
top = self.winfo_toplevel()
self.menuBar = tk.Menu(top)
top["menu"] = self.menuBar
self.subMenu = tk.Menu(self.menuBar)
self.menuBar.add_cascade(label="Help", menu=self.subMenu)
self.subMenu.add_command(label="About", command=clicked)


self.mainloop()
