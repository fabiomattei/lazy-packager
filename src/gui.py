import os
import tkinter as tk
from tkinter.filedialog import askdirectory

class Gui(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        """
        Constructor of main window
        it is made by:
        ttk.Entry containing the zip package name
        ttk.Treeview containing files and folders that belongs to the project
        tk.Button for changing folder
        tk.Button for generating the zip file
        """
        # initializing main window
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        # initializing dictionary that is going to contain all frames
        self.frames = {}
        # adding all necessary frames to the dictionary
        for F in (BrowsePage, FilesPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        # ginving control to the first frame
        self.show_frame("BrowsePage", 'Select the project directory containing all files')

    def show_frame(self, page_name, labText):
        """
        It shows the selected frame contained in the dictionary and
        initialize its lable with the labText
        
        :param page_name   string that allows to take the page from the dictionary self.frames
        :param labText     lable initializer
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
        