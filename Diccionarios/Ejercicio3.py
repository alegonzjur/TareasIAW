# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:42:30 2023

@author: agonjur
"""

#----Ejercicio 3----
f = str(input('Introduzca una fruta:'))
k = float(input('Introduzca un pesaje:'))
frutas = {'Platano':1.35,'Manzana':0.80,'Pera':0.85, 'Naranja':0.70}

if f in frutas.keys():
    print(k*frutas[f])
else:
    print('Esa fruta no está disponible.')