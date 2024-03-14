from flask import render_template
from app import app

@app.route("/")
def index():
    return render_template('index.html', title="App Facturación")

@app.route("/clientes")
def clientes():
    return render_template('clientes.html', title="Lista de Clientes")

@app.route("/form_cliente")
def form_cliente():
    return render_template('form_cliente.html', title="Formulario de Clientes")