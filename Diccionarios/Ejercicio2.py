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
dicc = {'nombre': n, 'edad': e, 'direccion':d, 'telefono':t}
print(dicc['nombre'], 'tiene', dicc['edad'],'años, vive en', 
      dicc['direccion'],'y su numero de telefono es', dicc['telefono'])