import os
import tkinter as tk
from tkinter.filedialog import askdirectory

class Gui(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        for F in (BrowsePage, FilesPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("BrowsePage", 'Seleziona una directory da Zippare, Pigro!')

    def show_frame(self, page_name, labText):
        """
        :param page_name (spiega cosa e' questo parametro)
        :param labText   (spiega cosa e' questo parametro)

        Change the content of the label
        """
        frame = self.frames[page_name]
        frame.label.config(text = labText )
        frame.tkraise()


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
        button = tk.Button(self, text="Sfoglia", command = self.files_pag)
        button.pack()
    
    def files_pag(self):
        """
        Callback linked to Sfoglia button.
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

class FilesPage(tk.Frame):

    def __init__(self, parent, controller):
        """Constructor of files page, it creates a label and a button"""
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="")
        self.label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Cambia Label", command = self.change_label)
        button.pack()
    
    def change_label(self):
        """This function changes the text of the label to CAMBIATA"""
        self.label.config(text = 'CAMBIATA')