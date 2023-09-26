import flask
from config import Config
from api_v1.auth_routes import auth_bp as auth_v1

auth_app = flask.Flask('__name__')
auth_app.register_blueprint(auth_v1, url_prefix='/api/v1')


if __name__ == '__main__':
    auth_app.run(debug=Config.DEBUG, port=5000)
    