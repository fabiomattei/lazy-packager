import tkinter as tk

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
        