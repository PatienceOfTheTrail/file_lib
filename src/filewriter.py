# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 22:08:27 2025

@author: PatienceOfTheTrail
"""

"""FileWriter class - All operations connected to files: writing and deleting"""

from datetime import date
import os
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
    
    def remove_old_file_lib(self):
        try:
            os.remove(self.datainterface.file_lib)
        except Exception as e:
            print("!ERROR! removing old file_lib.feather file")
            logger.error(f"Error removing old file_lib.feather file: {e}")
    
    def clear_text_file(self, text_file):
        try: 
            with open(text_file, mode= "w") as file:
                file.write("")    
        except Exception as e:
                print("!ERROR! while clearing text libraries.")
                logger.error(f"Error while clearing text libraries: {e}")
        
    def clear_files(self):
        while True:
            answer = input("Do you want to clear the files before extracting a new folder? (Y/N) ")
            if answer.lower() == "y":
                for text_file in self.clear_list:
                    self.clear_text_file(text_file)
                self.remove_old_file_lib()   
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
    
    def write_to_feather(self):
        try:
            self.datainterface.dataframe.to_feather(self.datainterface.file_lib)
        except Exception as e:
            print("!ERROR! creating feather library")
            logger.error(f"Error creating feather library: {e}")