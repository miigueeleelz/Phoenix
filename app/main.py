from flask import Flask
from flask_restful import Api

from resources import GenericResource

app = Flask(__name__)
api = Api(app)

api.add_resource(GenericResource, '/')
