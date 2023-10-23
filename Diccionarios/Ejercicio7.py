# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 11:08:45 2023

@author: agonjur
"""

#----Ejercicio 7----

dicc = dict()
introducir = True
while introducir == True:
    clave = str(input("Introduzca el producto:"))
    valor = float(input("Introduzca un precio:"))
    dicc[clave] = valor
    introducir = input("Algún dato más?") == "Si"
    
dicc['Total'] = sum(dicc.values())
print(dicc)