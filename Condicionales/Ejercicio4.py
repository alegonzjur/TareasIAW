# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 11:58:43 2023

@author: agonjur
"""

#----Ejercicio 4----#

a = input("Introduzca un primer número:")
b = input("Introduzca un segundo número:")
c = input("Introduzca un tercer número:")

if a>=b and a>=c:
    print("El valor más alto es A")
elif b>=a and b>=c:
    print("El valor más alto es B")
elif c>=a and c>=b:
    print("El valor más alto es C")
