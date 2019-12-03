# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:47:06 2019

@author: stefan
"""
import random 
import numpy as np
from rechteck import Rechteck
from Kreis import Kreis

print(Rechteck(1,8).flaeche())
print(Rechteck(5,1).umfang())
print(Kreis(2).Flaeche())
print(Kreis(5).Umfang())

#Zufallszahl zwischen 1 und 50 generieren:

def Number():
    return random.randint(1,50)

#Liste mit zufälligen Kreisen und Rechtecken generieren:
List_10 = []
for i in range(10):
    Z = random.choice(['Rechteck','Kreis'])
    List_10.append(Z)
    
#Listen für A und U der erzeuten Rechtecke und Kreise:
Kreis_A = []
Kreis_U = []
Rechteck_A = []
Rechteck_U = []
#Über die List_10 interieren und ergebnisse mithilfe der importierten Klassen ausrechnen und in die eingefühten Listen anfügen.
for i in List_10:
    if i == 'Kreis':
        radius = Number()
        r = Kreis(radius)
        Kreis_A.append(r.Flaeche())
        Kreis_U.append(r.Umfang())
    elif i == 'Rechteck':
        breite = Number()
        laenge = Number()
        b = Rechteck(breite,laenge)
        Rechteck_A.append(b.flaeche())
        Rechteck_U.append(b.umfang())
        
print('Es sind ' + str(List_10.count('Kreis')) + ' Kreise und ' + str(List_10.count('Rechteck')) + ' Rechtecke erzeugt worden')
print('Der durchschnittliche Umfang der Keise beträgt ' + str(np.mean(Kreis_U)))
print('Der durchschnittliche Umfange der Rechtecke beträgt ' + str(np.mean(Rechteck_U)))