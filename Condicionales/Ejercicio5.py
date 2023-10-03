# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 12:08:37 2023

@author: agonjur
"""

#----Ejercicio 5----#

dia_semanal = input("Introduzca un dia de la semana en minuscula:")
semana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
if dia_semanal in semana:
    print("El dia de la semana es", dia_semanal)
else:
    print("El dia introducido no existe.")
    
