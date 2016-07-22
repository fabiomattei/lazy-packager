import tkinter as tk
from tkinter import ttk
import os

class FilesPage(tk.Frame):

    def __init__(self, parent, controller):
        """Constructor of files page, it creates a label and a button"""
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="")
        self.label.pack(side="top", fill="x", pady=10)
        self.tree = ttk.Treeview(self)
        ysb = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(self, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.pack()
        button = tk.Button(self, text="Cambia Label") # , command = self.set_path
        button.pack()
        
    def set_path(self, path):
        self.tree.heading('#0', text=path, anchor='w')
        abspath = os.path.abspath(path)
        root_node = self.tree.insert('', 'end', text=abspath, open=True)
        self.process_directory(root_node, abspath)
    
    def process_directory(self, parent, path):
        for p in os.listdir(path):
            abspath = os.path.join(path, p)
            isdir = os.path.isdir(abspath)
            oid = self.tree.insert(parent, 'end', text=p, open=False)
            if isdir:
                self.process_directory(oid, abspath)

