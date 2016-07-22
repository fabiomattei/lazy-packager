import tkinter as tk
from src.gui.browserpage import BrowsePage
from src.gui.filespage import FilesPage

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
        
    def set_path(self, page_name, path):
        frame = self.frames[page_name]
        frame.set_path(path)
        

