from flask import render_template
from src.app import app
from src.models.clientes import Clientes
from flask_controller import FlaskController


class ClientesController(FlaskController):
    @app.route("/clientes")
    def clientes():
        return render_template('clientes.html', title="Lista de Clientes")
    
    @app.route("/clientes/<id>")
    def cliente_por_id(id):
        cliente = Clientes.obtener_cliente_por_id(id)
        return cliente

    @app.route("/form_cliente")
    def form_cliente():
        return render_template('form_cliente.html', title="Formulario de Clientes")