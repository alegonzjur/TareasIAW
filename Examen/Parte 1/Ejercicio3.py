# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:29:16 2023

@author: agonjur
"""

#Ejercicio 3

vocales = ['A','E','I','O','U','a','e','i','o','u']
letra = str(input("Introduzca un caracter:"))

if letra in vocales:
    print("El caracter", letra, "es una vocal.")
else:
    print("El caracter", letra, "no es una vocal.")
