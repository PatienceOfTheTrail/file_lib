# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 21:15:52 2025

@author: Jan
"""


"""Pandas Operations"""

import pandas as pd

class DataframeOperator():
    def __init__(self, datainterface):
        self.datainterface = datainterface
    
    def adjust_dict(self):
        longest_key = max(self.datainterface.data_dict, 
                          key=lambda k: len(self.datainterface.data_dict[k]))
        
        for key in self.datainterface.data_dict.keys():
            if not key is longest_key:
                while True:
                    self.datainterface.data_dict[key].append(None)
                    if len(self.datainterface.data_dict[key]) == len(self.datainterface.data_dict[longest_key]):
                           break
    
    def create_dataframe(self):
        self.datainterface.dataframe = pd.DataFrame(self.datainterface.data_dict)
        
    
    