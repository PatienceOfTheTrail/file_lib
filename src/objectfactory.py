# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 22:58:36 2025

@author: Jan
"""

from src.logger import logger
import sys

class ObjectFactory:
    @staticmethod
    def create_file_object(class_, file, datainterface):
        try:
            obj = class_(file, datainterface)
            return obj
        except Exception as e:
            print("An unforeseen error occured in ObjectFactory!")
            print(f"{e}")
            logger.error("Error in ObjectFactory", exc_info=True)
            print("Program will be terminated.")
            sys.exit()