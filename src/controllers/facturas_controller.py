from flask import render_template, request, redirect, url_for
from src.app import app
from src.models.facturas import Facturas
from src.models.clientes import Clientes
from flask_controller import FlaskController
import datetime


class FacturasController(FlaskController):
    
    @app.route("/agregar_factura", methods=['GET','POST'])    
    def agregar_factura():
        if request.method == 'POST':
            fecha = request.form.get('fecha')
            cliente = request.form.get('identificacion')
            factura = Facturas(fecha,cliente)
            Facturas.agregar_factura(factura)
            return redirect(url_for('facturas'))        
        clientes = Clientes.obtener_clientes()
        fecha = datetime.datetime.now()
        return render_template("formulario_factura.html", clientes=clientes, fecha=fecha)

    @app.route("/facturas")
    def facturas():
        facturas = Facturas.obtener_facturas()
        return render_template("facturas.html",facturas=facturas)