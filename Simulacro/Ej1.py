# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:57:16 2023

@author: agonjur
"""

introducir = True
lista = []
mult = 1
while introducir == True:
    entero = int(input("Introduzca un numero entero:"))
    lista.append(entero)
    mult = mult * entero
    introducir = input("¿Quiere seguir introduciendo numeros?") == "Si"

'''for i in lista:
    sumatorio += x
    multipliacion *= x'''
print("La suma de los números introducidos es ", sum(lista))
print("La multiplicacion de los numeros introducidos es", mult)
    
