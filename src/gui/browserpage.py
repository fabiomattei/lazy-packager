import tkinter as tk
import os
from tkinter.filedialog import askdirectory

class BrowsePage(tk.Frame):
    
    def __init__(self, parent, controller):
        """
        Constructor of Browse page.
        it is made by a label that will contain the file names
        and a button that reload files
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="")
        self.label.pack(side="top", fill="x", pady=10)
        self.names = []
        button = tk.Button(self, text="Select project folder", command = self.files_pag)
        button.pack()
    
    def files_pag(self):
        """
        Callback linked to "Select project folder" button.
        walk in to a directory and put all files in the label.
        """
        folder = askdirectory()
        self.label.config(text="")
        for path, dirs, files in os.walk(folder):
            self.names.append(path)
            self.names.append('\n')
            for f in files:
                self.names.append(f)
                self.names.append('\n')
        self.controller.show_frame("FilesPage", self.names)
