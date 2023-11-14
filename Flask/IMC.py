# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:02:31 2023

@author: agonjur
"""
#El HTML de esta tarea es "index_1.html."
from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/", methods=["POST", "GET"])

def imc():
    peso = ""
    altura = ""
    comentario = ""
    if (request.method == 'POST'):
        peso = float(request.form.get("peso"))
        altura = float(request.form.get("altura"))
        imc = peso/(altura*altura)
        print(peso, altura, imc)
        if imc < 18.5:
            comentario = ('Con', altura, 'm. de altura y ', peso,'kg de peso tu imc es', imc,', que es un IMC bajo.')
        elif (18.5<imc<24.9):
            comentario = ('Con', altura, 'm. de altura y ', peso,'kg de peso tu imc es', imc,', que es un IMC normal.')
        elif 25<imc<29.9:
            comentario = ('Con', altura, 'm. de altura y ', peso,'kg de peso tu imc es', imc,', que es un IMC de sobrepeso.')
        else:
            comentario = ('Con', altura, 'm. de altura y ', peso,'kg de peso tu imc es', imc,', que es un IMC de obesidad.')
    return render_template("index_1.html", comentario=comentario)

app.run()
