# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:13:43 2019

@author: stefa
"""
class Rechteck:
    def __init__(self, Länge, Breite):
        self.length = Länge
        self.width = Breite
    def flaeche(self):
        area = self.length * self.width
        return area
    def umfang(self):
        umf = 2 * self.length +2*self.width
        return umf

        
        
