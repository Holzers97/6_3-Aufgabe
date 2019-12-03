# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:39:25 2019

@author: stefa
"""
import numpy as np

class Kreis:
    def __init__(self,Radius):
        self.radius = Radius
        
    def Flaeche(self):
        flae = (self.radius**2) * np.pi
        return flae
    
    def Umfang(self):
        umf = 2*(self.radius)* np.pi
        return umf
    
        
