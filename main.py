from flask import Flask, render_template
from flask import jsonify
from config import config
from models import db
from models import Servicio, Hotel, Restaurant, Atraccion, Lista

def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app

enviroment = config['development']
app = create_app(enviroment)

@app.route('/img/<folder>/<filename>')
def show_img(folder,filename):
    filename = 'http://127.0.0.1:5000/static/images/' + folder + '/' + filename
    return render_template('img.html', filename=filename)

@app.route('/api/v1/hotels', methods=['GET'])
def get_hotels():
    hotels = [hotel.json() for hotel in Servicio.query.join(Hotel).all()]
    return jsonify({'hotels': hotels })

@app.route('/api/v1/hotels/<cod_hotel>', methods=['GET'])
def get_hotel(cod_hotel):
    hotel = Servicio.query.filter_by(id_servicio=cod_hotel).first()
    if hotel is None:
        return jsonify({'message': 'El hotel no existe'}), 404
    return jsonify({'hotel': hotel.json() })

@app.route('/api/v1/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = [restaurant.json() for restaurant in Servicio.query.join(Restaurant).all()]
    return jsonify({'restaurants': restaurants })

@app.route('/api/v1/restaurants/<cod_restaurant>', methods=['GET'])
def get_restaurant(cod_restaurant):
    restaurant = Servicio.query.filter_by(id_servicio=cod_restaurant).first()
    if restaurant is None:
        return jsonify({'message': 'El restaurant no existe'}), 404
    return jsonify({'restaurant': restaurant.json() })

@app.route('/api/v1/atractions', methods=['GET'])
def get_atractions():
    atractions = [atraccion.json() for atraccion in Servicio.query.join(Atraccion).all()]
    return jsonify({'atractions': atractions })

@app.route('/api/v1/atractions/<cod_atraction>', methods=['GET'])
def get_atraction(cod_atraction):
    atraccion = Servicio.query.filter_by(id_servicio=cod_atraction).first()
    if atraccion is None:
        return jsonify({'message': 'La atracción no existe'}), 404
    return jsonify({'atraccion': atraccion.json() })

@app.route('/api/v1/lists', methods=['GET'])
def get_lists():
    lists = [lista.json() for lista in Lista.query.all()]
    return jsonify({'lists': lists })

if __name__ == '__main__':
    app.run(debug=True)
