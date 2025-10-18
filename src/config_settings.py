# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 01:05:15 2025

@author: PatienceOfTheTrail
"""

"""Configuration file"""

import os
import json

# init base directory of project
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# path to config json
config_json = os.path.join(BASE_DIR, "config", "config.json")

# Load lists from config json file
with open(config_json, mode="r") as file:
    data = json.load(file)
    documents_and_office = data["documents_and_office"]
    compressed_and_archive = data["compressed_and_archive"]
    pictures_and_media = data["pictures_and_media"]
    system_and_else = data["system_and_else"]
    
# paths to output files
documents_and_office_text = os.path.join(BASE_DIR, "data", "documents_and_office.txt")
compressed_and_archive_text = os.path.join(BASE_DIR, "data", "compressed_and_archive.txt")
pictures_and_media_text = os.path.join(BASE_DIR, "data", "pictures_and_media.txt")
system_and_else_text = os.path.join(BASE_DIR, "data", "system_and_else.txt")

file_lib = os.path.join(BASE_DIR, "data", "file_lib.feather")