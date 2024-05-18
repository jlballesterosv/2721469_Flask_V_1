from flask import Flask
from src.models import Base, engine
from flask_controller import FlaskControllerRegister

app = Flask(__name__)


register = FlaskControllerRegister(app)
register.register_package('src.controllers')

Base.metadata.create_all(engine)


if __name__ == '__main___':
    app.run(debug=True)