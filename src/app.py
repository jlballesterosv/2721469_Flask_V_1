from flask import Flask

app = Flask(__name__)

from controller import *

if __name__ == '__main___':
    app.run(debug=True)