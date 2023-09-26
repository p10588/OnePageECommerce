import flask
from config import Config
from Api_v1.shop_routes import shop_bp as shop_v1

shop_app = flask.Flask('__name__')
shop_app.register_blueprint(shop_v1, url_prefix='/api/v1')


if __name__ == '__main__':
    shop_app.run(debug=Config.DEBUG, port=5002)
    