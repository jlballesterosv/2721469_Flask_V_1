from flask import Flask
from models import Base, engine

app = Flask(__name__)


from controllers import *
Base.metadata.create_all(engine)


if __name__ == '__main___':
    app.run(debug=True)