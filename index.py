from flask import Flask


app = Flask(__name__)

from controllers.ApiController import *

if __name__ == '__main__':
    app.run(debug=True)
