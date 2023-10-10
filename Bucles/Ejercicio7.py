# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:08:38 2023

@author: agonjur
"""

#----Ejercicio 7----

contraseña = str(input("Introduzca la contraseña:"))
palabra = 'Quitamanchas'

while contraseña != palabra:
    print("Contraseña incorrecta.")
    contraseña = str(input("Introduzca otra contraseña."))

if contraseña == palabra:
    print("Bienvenido.")
