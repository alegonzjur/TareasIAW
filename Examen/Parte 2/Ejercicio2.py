# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:45:56 2023

@author: agonjur
"""

#Ejercicio 2
lista_meses = [['Enero','31'],['Febrero','28'],['Marzo','31'],
               ['Abril','30'],['Mayo','31'],['Junio','30'],['Julio','31'],
               ['Agosto','31'],['Septiembre','30'],['Octubre','31'],
               ['Noviembre','30'],['Diciembre','31']]
mes_intro = int(input("Introduzca un mes en número (1-12):"))
mes_lista = mes_intro-1
print("El mes", mes_intro,"es", lista_meses[mes_lista][0],'y tiene', 
      lista_meses[mes_lista][1],'días.')

