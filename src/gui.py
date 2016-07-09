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
        frame = self.frames[page_name]
        frame.label.config(text = labText )
        frame.tkraise()


class BrowsePage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="")
        self.label.pack(side="top", fill="x", pady=10)
        self.names = []
        button = tk.Button(self, text="Sfoglia", command = self.files_pag)
        button.pack()
    
    def files_pag(self):
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
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="")
        self.label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Cambia Label", command = self.change_label)
        button.pack()
    
    def change_label(self):
        self.label.config(text = 'CAMBIATA')