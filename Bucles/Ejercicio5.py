# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:36:44 2023

@author: agonjur
"""

#----Ejercicio 5----

inversion = float(input("Cantidad a invertir:"))
interes = float(input("Interes anual:"))
duracion = int(input("Numero de años:"))
contador = 1

lista = []
while contador <= duracion:
    lista.append(inversion+inversion*interes*contador)
    contador = contador + 1

print(lista)