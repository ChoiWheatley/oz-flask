"""
https://flask-restful.readthedocs.io/en/latest/
"""

from flask import Flask, request
from flask_restful import Resource, Api

from resources.item import Item

app = Flask(__name__)
api = Api(app)
api.add_resource(Item, "/item/<string:name>")  # add path

if __name__ == "__main__":
    app.run(debug=True)
