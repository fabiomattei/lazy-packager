#!/usr/bin/python3

'''
Created on the 9th of July 2016
@author: Fabio Mattei, Tommaso
'''

from tkinter import *
from src.gui import Gui
            
def main():            
    
    root = Tk()
    app = Gui(root)
    root.mainloop()
    
if __name__ == "__main__": main()
