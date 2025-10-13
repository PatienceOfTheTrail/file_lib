# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 22:08:27 2025

@author: Jan
"""

from datetime import date
import sys

from src.logger import logger

class FileWriter():
    __current_date = str(date.today())
    
    def __init__(self, datainterface):
        self.datainterface = datainterface
        
        self.run_list = [
            (self.datainterface.documents_and_office_list,
             self.datainterface.documents_and_office_text),
            (self.datainterface.compressed_and_archive_list,
             self.datainterface.compressed_and_archive_text),
            (self.datainterface.pictures_and_media_list,
             self.datainterface.pictures_and_media_text),
            (self.datainterface.system_and_else_list,
             self.datainterface.system_and_else_text)
                         ]
    
        self.clear_list = [
            self.datainterface.documents_and_office_text,
            self.datainterface.compressed_and_archive_text,
            self.datainterface.pictures_and_media_text,
            self.datainterface.system_and_else_text
            ]
    
    def clear_files(self):
        while True:
            answer = input("Do you want to clear the files before extracting a new folder? (Y/N) ")
            if answer.lower() == "y":
                for text_file in self.clear_list:
                    with open(text_file, mode= "w") as file:
                        file.write("")           
                print("All files are cleared!")
                print("")
                break
            elif answer.lower() == "n":
                print("New entries will be appended to already existing ones.")
                break
            else:
                print("Invalid answer! Please enter 'Y' or 'N'!" )
    
    def write_header(self, file):
        file.write("NEW ENTRY\n")
        file.write(f"Extracted Folder: {self.datainterface.folder}\n")
        file.write(f"Date: {FileWriter.__current_date}\n")
        file.write("File Paths:\n")
    
    def write_to_text_files(self):
        for list_, text_file in self.run_list:
            if list_:
                with open(text_file, mode="a") as file:
                    self.write_header(file)
                    for i in list_:
                        file.write(f"- {i}\n")
                    file.write("_________________________________________________\n")
            