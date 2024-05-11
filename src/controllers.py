from flask import render_template, request, redirect, url_for
from app import app
from models import Productos, Categorias

@app.route("/")
def index():
    return render_template('index.html', title="App Facturación")

@app.route("/clientes")
def clientes():
    return render_template('clientes.html', title="Lista de Clientes")

@app.route("/form_cliente")
def form_cliente():
    return render_template('form_cliente.html', title="Formulario de Clientes")

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