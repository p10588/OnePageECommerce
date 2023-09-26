import flask
from config import Config
from api_v1.orders_routes import orders_bp as orders_v1

orders_app = flask.Flask('__name__')
orders_app.register_blueprint(orders_v1, url_prefix='/api/v1')


if __name__ == '__main__':
    orders_app.run(debug=Config.DEBUG, port=5003)