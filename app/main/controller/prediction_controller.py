from flask import request
from flask_restplus import Namespace, Resource, fields

from ..service.prediction_service import get_predictions

api = Namespace('Prediction', description='Prediction related operations')

text = api.model('Text', {
    'data': fields.List(fields.String)
})

prediction = api.model('Prediction', {
    'data': fields.List(fields.Integer),
})


@api.route('/')
class PredictionList(Resource):
    @api.doc('Retrieves a list of sentiment predictions for the supplied list of text strings')
    @api.expect(text)
    @api.response(200, 'Success', prediction)
    def post(self):
        return get_predictions(request.json)
