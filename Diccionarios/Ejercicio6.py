# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:53:14 2023

@author: agonjur
"""

#----Ejercicio 6----

dicc = dict()
introducir = True
while introducir == True:
    clave = str(input("Introduzca su clave:"))
    valor = str(input("Introduzca su valor:"))
    dicc[clave] = valor
    print(dicc)
    introducir = input("¿Algun dato mas?") == "Si"