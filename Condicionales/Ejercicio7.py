# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 12:21:30 2023

@author: agonjur
"""

#----Ejercicio 7----#

edad = int(input("Introduzca su edad:"))
ingresos_men = float(input("Introduzca sus ingresos mensuales:"))

if edad < 16 or ingresos_men<=1000:
    print("El usuario no tiene que tributar.")
else:
    print("El usuario tiene que tributar.")