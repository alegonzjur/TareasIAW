# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:22:05 2023

@author: agonjur
"""

#----Ejercicio 2----
n = str(input('Introduzca su nombre:'))
e = int(input('Introduzca su edad:'))
d = str(input('Introduzca su direccion:'))
t = int(input('Introduzca su telefono:'))
dicc = dict()
dicc['nombre'] = n
dicc['edad'] = e
dicc['direccion'] = d
dicc['telefono'] = t
print(dicc.get('nombre'), 'tiene', dicc.get('edad'),'años, vive en', 
      dicc.get('direccion'),'y su numero de telefono es', dicc.get('telefono'))