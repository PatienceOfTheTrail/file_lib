# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 23:15:39 2025

@author: PatienceOfTheTrail
"""

"""Error Logger"""

import logging

logger = logging.getLogger("main_logger")
logger.setLevel(logging.ERROR)

if not logger.hasHandlers():
    file_handler = logging.FileHandler(r'logs\error.log', mode='a')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)