# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 22:25:08 2025

@author: Jan
"""

"""DataInterface - for communication between classes and data storage"""
from dataclasses import dataclass, field
from typing import Optional
from src import config_settings

@dataclass
class DataInterface():
    # placeholder
    folder: Optional[str] = None
    files: list = field(default_factory=list)
    
    documents_and_office_list: list = field(default_factory=list)
    compressed_and_archive_list: list = field(default_factory=list)
    pictures_and_media_list: list = field(default_factory=list)
    system_and_else_list: list = field(default_factory=list)
    
    # data from config_json
    documents_and_office: list = field(default_factory=lambda:config_settings.documents_and_office)
    compressed_and_archive: list = field(default_factory=lambda:config_settings.compressed_and_archive)
    pictures_and_media :list = field(default_factory=lambda:config_settings.pictures_and_media)
    system_and_else: list = field(default_factory=lambda:config_settings.system_and_else)
    
    # file_paths
    documents_and_office_text: str = config_settings.documents_and_office_text
    compressed_and_archive_text: str = config_settings.compressed_and_archive_text
    pictures_and_media_text: str = config_settings.pictures_and_media_text
    system_and_else_text: str = config_settings.system_and_else_text
    
