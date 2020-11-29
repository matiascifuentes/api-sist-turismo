from flask import Flask
from flask import jsonify
from config import config
from models import db
from models import Hotel, Restaurant

def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app

enviroment = config['development']
app = create_app(enviroment)


@app.route('/api/v1/hotels', methods=['GET'])
def get_hotels():
    hotels = [hotel.json() for hotel in Hotel.query.all()]
    return jsonify({'hotels': hotels })

@app.route('/api/v1/hotels/<cod_hotel>', methods=['GET'])
def get_hotel(cod_hotel):
    hotel = Hotel.query.filter_by(cod_hotel=cod_hotel).first()
    if hotel is None:
        return jsonify({'message': 'El hotel no existe'}), 404
    return jsonify({'hotel': hotel.json() })

@app.route('/api/v1/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = [restaurant.json() for restaurant in Restaurant.query.all()]
    return jsonify({'restaurants': restaurants })

@app.route('/api/v1/restaurants/<cod_restaurant>', methods=['GET'])
def get_restaurant(cod_restaurant):
    restaurant = Restaurant.query.filter_by(cod_restaurant=cod_restaurant).first()
    if restaurant is None:
        return jsonify({'message': 'El restaurant no existe'}), 404
    return jsonify({'restaurant': restaurant.json() })

if __name__ == '__main__':
    app.run(debug=True)
