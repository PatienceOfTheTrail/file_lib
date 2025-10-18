# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 19:41:26 2025

@author: PatienceOfTheTrail
"""

"""All sorting logic"""

import os

class FileSorter():
    def __init__(self, file, datainterface):
        self.file = file
        self.datainterface = datainterface
        
        self.run_list = [(self.datainterface.documents_and_office, 
                          self.datainterface.documents_and_office_list),
                         (self.datainterface.compressed_and_archive,
                         self.datainterface.compressed_and_archive),
                         (self.datainterface.pictures_and_media,
                          self.datainterface.pictures_and_media_list),
                         (self.datainterface.system_and_else,
                         self.datainterface.system_and_else_list)]
        
    def split_file(self):
        base_name = os.path.basename(self.file)
        split_list = base_name.split(".")
        file_end = split_list[1]
        return file_end
    
    def add_to_dict(self, item):
        if not item in self.datainterface.data_dict.keys():
            self.datainterface.data_dict[item] = [self.file]
        elif item in self.datainterface.data_dict.keys():
            self.datainterface.data_dict[item].append(self.file)
    
    def sorting_loop(self, file_end):
        for end_list, empty_list in self.run_list:
            for item in end_list:
                if file_end == item:
                    if not file_end == ".gitkeep":
                        empty_list.append(self.file)
                        return item
    
    def main_run(self):
        file_end ="." + self.split_file()
        item = self.sorting_loop(file_end)
        if item is not None:
            self.add_to_dict(item)
        if not self.file == ".gitkeep":
            print(f"- {self.file} is processed.")
        
        