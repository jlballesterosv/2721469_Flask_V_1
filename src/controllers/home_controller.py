from flask import render_template, request, redirect, url_for
from src.app import app
from flask_controller import FlaskController


class HomeController(FlaskController):
    @app.route("/")
    def index():
        return render_template('index.html', title="App Facturación")