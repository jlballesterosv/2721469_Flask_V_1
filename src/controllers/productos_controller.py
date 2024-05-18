from flask import render_template, request, redirect, url_for
from src.app import app
from src.models.productos import Productos
from src.models.categorias import Categorias
from flask_controller import FlaskController


class ProductosController(FlaskController):
    @app.route("/agregar_producto", methods=['GET','POST'])
    def agregar_producto():
        if request.method == 'POST':
            descripcion = request.form.get('descripcion')
            valor_unitario = request.form.get('valor_unitario')
            cantidad_stock = request.form.get('cantidad_stock')
            unidad_medida = request.form.get('unidad_medida')
            categoria = request.form.get('categoria')
            productos = Productos(descripcion,unidad_medida,cantidad_stock,valor_unitario,categoria)
            Productos.agregar_producto(productos)
            return redirect(url_for('productos'))
        categorias = Categorias.obtener_categorias()
        return render_template("formulario_producto.html", categorias=categorias)

    @app.route("/productos")
    def productos():
        productos = Productos.obtener_productos()
        return render_template("productos.html",productos=productos)