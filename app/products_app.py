import flask
from config import Config
from api_v1.product_routes import product_bp as product_v1

product_app = flask.Flask('__name__')
product_app.register_blueprint(product_v1, url_prefix='/api/v1')

if __name__ == '__main__':
    product_app.run(debug=Config.DEBUG, port=5001)
    