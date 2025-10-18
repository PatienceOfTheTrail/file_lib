# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 22:03:49 2025

@author: PatienceOfTheTrail
"""

"""File Lib - main run"""

import sys
import time

from src.datainterface import DataInterface
from src.folderaccess import FolderReader
from src.objectfactory import ObjectFactory
from src.filesorter import FileSorter
from src.filewriter import FileWriter
from src.dataframe_operator import DataframeOperator

def main():
    print("File Library - Extract files from folder and write in library")
    print("_____________________________________________________________")
    datainterface = DataInterface()
    folderreader = FolderReader(datainterface)
    filewriter = FileWriter(datainterface)
    filewriter.clear_files()
    
    folderreader.read_folder()
    folderreader.get_files_from_folder()
    
    for file in datainterface.files:
        filesorter = ObjectFactory.create_file_object(FileSorter, file, datainterface)
        filesorter.main_run()
    
    # dataframe operations
    dataframe_operator = DataframeOperator(datainterface)
    dataframe_operator.adjust_dict()
    dataframe_operator.create_dataframe()
    
    filewriter.write_to_text_files()
    filewriter.write_to_feather()
    
    print("")
    print("Files added to text file libraries.")
    print("Feather library file created.")
    print("Program will be terminated.")
    
    time.sleep(2)
    sys.exit()
    
if __name__ == "__main__":
    main()
    