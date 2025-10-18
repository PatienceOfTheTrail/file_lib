# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 22:19:13 2025

@author: PatienceOfTheTrail
"""

"""FolderReader - Reads folder, extracts files and pushes data to datainterface"""

import os
from tkinter import filedialog
import sys

class FolderReader():
    def __init__(self, datainterface):
        self.datainterface = datainterface
    
    # get folder from user
    def read_folder(self):
        print("Please select your folder!")
        self.datainterface.folder = filedialog.askdirectory()
        x = self.datainterface.folder
        
        if x == "":
            print("No folder was selected!")
            print("The program will be terminated.")
            sys.exit()
            
        print(f"Your folder: {x}")
        print("")
        
    def get_files_from_folder(self):
        print("Extracting files from folder:")
        self.datainterface.files = os.listdir(self.datainterface.folder)
        if ".gitkeep" in self.datainterface.files:
            self.datainterface.files.remove(".gitkeep")
    
        
        