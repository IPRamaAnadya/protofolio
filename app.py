# import library
from pyexpat import model
from flask import Flask, render_template, request
from flask_restful import Resource, Api
from flask_cors import CORS
import os

# init object flask
app = Flask(__name__)

# init object flask restfull
api = Api(app)

# init cors
CORS(app)



@app.route("/")
def landing():
    return render_template("/index.html")


if __name__ == "__main__":
    app.run(debug=True, port = int(os.environ.get('PORT', 5000)))