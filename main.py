from flask import Flask, render_template
from flask import jsonify
from flask import request
from config import config
from models.database import db
from models.database import Servicio, Hotel, Restaurant, Atraccion, Lista, DetalleLista, Sesion, PagVisitada, Usuario
from datetime import datetime
from recommendation_system.utils import get_itemset_historico_listas
from recommendation_system.recommendation_system import generate_association_rules, recommendations, save_rules_to_file, get_rules_from_file

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
    return jsonify({'atraction': atraccion.json() })

@app.route('/api/v1/lists', methods=['GET'])
def get_lists():
    lists = [lista.json() for lista in Lista.query.all()]
    return jsonify({'lists': lists })

@app.route('/api/v1/lists/<cod_lista>', methods=['GET'])
def get_list(cod_lista):
    lista = Lista.query.filter_by(id_lista=cod_lista).first()
    if lista is None:
        return jsonify({'message': 'La lista no existe'}), 404
    return jsonify({'lista': lista.json() })

@app.route('/api/v1/lists', methods=['POST'])
def add_list():
    if not request.json or not 'id_usuario' in request.json or not 'servicios' in request.json:
        return jsonify({'error':'error de datos'}),400
    id_usuario = request.json['id_usuario']
    servicios = request.json['servicios']
    now = datetime.now()
    fecha = now.strftime("%d-%m-%Y %H:%M:%S")
    lista = Lista(id_usuario=id_usuario,fecha=fecha)
    db.session.add(lista)
    db.session.commit()
    id_lista = lista.json()['id_lista']
    if id_lista:
        for servicio in servicios:
            detalle = DetalleLista(id_lista=id_lista, id_servicio=servicio['id_servicio'])
            db.session.add(detalle)
            db.session.commit()
        return jsonify({'success': id_lista})
    return jsonify({'error': 'error'})
   

@app.route('/api/v1/details', methods=['GET'])
def get_details():
    details = [detalle.json() for detalle in DetalleLista.query.all()]
    return jsonify({'details': details })

@app.route('/api/v1/details/<cod_lista>', methods=['GET'])
def get_detail(cod_lista):
    details = [detalle.json() for detalle in DetalleLista.query.filter_by(id_lista=cod_lista).all()]
    if details is None:
        return jsonify({'message': 'La lista no existe'}), 404
    return jsonify({'detalle': details })

@app.route('/api/v1/sesions', methods=['GET'])
def get_sesions():
    sesions = [sesion.json() for sesion in Sesion.query.all()]
    return jsonify({'sesions': sesions })

@app.route('/api/v1/sesions/<cod_sesion>', methods=['GET'])
def get_sesion(cod_sesion):
    sesion = Sesion.query.filter_by(id_sesion=cod_sesion).first()
    if sesion is None:
        return jsonify({'message': 'La sesión no existe'}), 404
    return jsonify({'sesion': sesion.json() })

@app.route('/api/v1/pages', methods=['GET'])
def get_pages():
    pages = [pagina.json() for pagina in PagVisitada.query.all()]
    return jsonify({'pages': pages })

@app.route('/api/v1/users/<correo>/byemail', methods=['GET'])
def get_user_email(correo):
    user = Usuario.query.filter_by(correo=correo).first()
    if user is None:
        return jsonify({'message': 'El usuario no existe'})
    return jsonify({'user': user.json() })

@app.route('/api/v1/users/<id>/byid', methods=['GET'])
def get_user_id(id):
    user = Usuario.query.filter_by(id_usuario=id).first()
    if user is None:
        return jsonify({'message': 'El usuario no existe'})
    return jsonify({'user': user.json() })

@app.route('/api/v1/recommendations/<service_id>', methods=['GET'])
def get_recommendations(service_id):
    success, rules = get_rules_from_file()
    if(success):
        result = recommendations(service_id,rules,10)
        return jsonify({'recommendations': result })
    return jsonify({'error': 'no se encontraron reglas'})


if __name__ == '__main__':
    app.run(debug=True)
