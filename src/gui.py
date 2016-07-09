import os
from tkinter import ttk
from tkinter.filedialog import askdirectory


class Gui:

    def __init__(self, master):

        self.label = ttk.Label(master, text = "Hello, Tkinter!")
        self.label.grid(row = 0, column = 0, columnspan = 3)
        
        ttk.Button(master, text = "Texas",
                   command = self.texas_hello).grid(row = 1, column = 0)

        ttk.Button(master, text = "Hawaii",
                   command = self.hawaii_hello).grid(row = 1, column = 1)

        ttk.Button(master, text = "Decartellami",
                   command = self.browse_hello).grid(row = 1, column = 2)

    def texas_hello(self):
        self.label.config(text = 'Howdy, Tkinter!')

    def hawaii_hello(self):
        self.label.config(text = 'Aloha, Tkinter!')
        
    def browse_hello(self):
        folder = askdirectory()
        names = []
        for path, dirs, files in os.walk(folder):
            names.append(path)
            names.append('\n')
            for f in files:
                names.append(f)
                names.append('\n')
        self.label.config(text = names)