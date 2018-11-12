from flask_restplus import Api
from flask import Blueprint

blueprint = Blueprint('sentiment-analysis-api', __name__)
api = Api(blueprint, title='Sentiment Analysis API', version='1.0')


