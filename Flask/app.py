# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 10:40:17 2023

@author: agonjur
"""

from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/', methods=['POST','GET'])
def hola():
    user = request.form.get("usuario")
    password = request.form.get("contrasena")
    print(user, " ",  password)
    return render_template("index.html", user=user, password=password)


@app.route("/baloncesto")
def baloncesto():
    return "Esta es la web de Baloncesto."

@app.route("/pruebaPost", methods=['POST','GET'])
def pruebaPost():
    if (request.method == 'POST'):
        return "Esto es un POST"
    elif (request.method == 'GET'):
        return "Esto es un GET."
    return "Esta es la web de baloncesto."
 
app.run()

