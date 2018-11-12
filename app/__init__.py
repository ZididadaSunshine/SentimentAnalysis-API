from flask_restplus import Api
from flask import Blueprint
from .main.controller.prediction_controller import api as prediction_ns

blueprint = Blueprint('sentiment-analysis-api', __name__)
api = Api(blueprint, title='Sentiment Analysis API', version='1.0')

api.add_namespace(prediction_ns, path='/prediction')
