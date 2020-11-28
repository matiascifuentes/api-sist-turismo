from flask import Flask
from flask import jsonify
from config import config
from models import db
from models import Hotel

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

if __name__ == '__main__':
    app.run(debug=True)
