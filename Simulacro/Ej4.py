# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:26:39 2023

@author: agonjur
"""

introducir = True
dicc = dict()
while introducir == True:
    n = str(input("Introduzca su nombre:"))
    e = int(input("Introduzca su edad:"))
    s = str(input("Introduzca su genero:"))
    t = int(input("Introduzca su telefono:"))
    c = str(input("Introduzca su correo:"))
    dicc = {"nombre":n,'edad':e,'sexo':s,'telefono':t,'correo':c}
    print(dicc)
    introducir = input('¿Desea introducir más datos?') == 'Si'
