from flask import Blueprint

auth_bp = Blueprint('auth_v1', __name__)

@auth_bp.route('/auth/login')
def Login():
    return 'Login' 

    
@auth_bp.route('/auth/signin')
def SignIn():
    return 'Signin'


@auth_bp.route('/auth/signout')
def SignOut():
    return 'SignOut'