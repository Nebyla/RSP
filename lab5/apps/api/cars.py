from flask import abort
from flask_restx import Namespace, Resource, fields
from flask_restx.reqparse import RequestParser
from ..models import cars
from flask import request, abort, current_app
from sqlalchemy.exc import IntegrityError
from ..database import db

ns = Namespace(name='car', description='Car operations')

cars_expect_model = ns.model('Car expect', {
    'CarName': fields.String(),
    'dateRelease': fields.String(),
    'genre': fields.String(),
    'urlImage': fields.String(),
})

cars_response_model = ns.model('Car response', {
    'id': fields.Integer(),
    'carName': fields.String(),
    'dateRelease': fields.String(),
    'genre': fields.String(),
    'urlImage': fields.String(required=True),
    'dateJoined': fields.DateTime(),
})


@ns.route('')
class CarsApi(Resource):
    @ns.marshal_list_with(cars_response_model)
    def get(self):
        cars = cars.query.all()
        return cars
    
    @ns.marshal_list_with(cars_response_model)
    @ns.expect(cars_expect_model)
    def post(self):
        data = ns.payload
        
        new_cars = cars(**data)

        try:
            new_cars.save()
        except IntegrityError as e:
            current_app.logger.error(e)
            abort(400, str(e.orig))

        return new_cars, 201

@ns.route('/<id>')
@ns.param('id', 'The unique identifier of a Product')
class CarsApiById(Resource):
    @ns.marshal_with(cars_response_model)
    def get(self, id):
        cars = cars.query.get_or_404(id, 'cars not found')
        return cars
    
    @ns.expect(cars_expect_model)
    @ns.marshal_with(cars_response_model)
    def put(self, id):
        cars = cars.query.get_or_404(id, 'cars not found')
        data = ns.payload

        try:
            cars.update(data)
        except IntegrityError as e:
            current_app.logger.error(e)
            abort(400, str(e.orig))

        return cars

    @ns.response(204, 'cars deleted')
    def delete(self, id):
        cars = cars.query.get_or_404(id, 'cars not found')
        db.session.delete(cars)
        db.session.commit()
        return '', 204
