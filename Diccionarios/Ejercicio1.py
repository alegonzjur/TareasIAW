# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:14:02 2023

@author: agonjur
"""

#----Ejercicio 1----
dicc = dict()
dicc['Euro'] = '€'
dicc['Dollar'] = '$'
dicc['Yen'] = 'Y'
divisa = str(input('Introduzca una divisa:'))
if divisa in dicc:
    print('El simbolo de',divisa,'es',dicc.get(divisa))
else:
    print('La divisa no se encuentra en el diccionario.')

