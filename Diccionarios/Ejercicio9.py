# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:21:35 2023

@author: agonjur
"""

#----Ejercicio 9----#
dicc = dict()
añadir = True
pagar = True
contador = 0
añadir = input("Desea añadir alguna factura?") == "Si"
while añadir == True:
    clave = int(input("Introduzca el numero de factura:"))
    valor = float(input("Introduzca el coste de la factura:"))
    dicc[clave] = valor
    añadir = input("Desea añadir alguna factura?") == "Si"
pagar = input("Desea pagar alguna factura?") == "Si"
while pagar == True:
    clave = int(input("Introduzca el numero de factura"))
    contador += dicc[clave]
    dicc.pop(clave)
    pagar = input("Desea pagar alguna factura?") == "Si"
print("La cantidad pagada es", contador)
print("La cantidad a pagar es", sum(dicc.values()))
    