import pytest
from db.user_repo_postgres import UserRepo_postgres
from models.user_model import User


def test_add_new_user():
    user = User(
        user_id='0',
        full_name='sample name',
        account='aaa',
        email='aaa@aaa.com',
        shipping_address='qwertyuiop',
        contact_phone='+88612345678'
    )
    try:
        user_repo = UserRepo_postgres()
        user_repo.add_new_user(user)
        assert True
    except Exception as e:
        print(e)
        assert False

def test_update_user_data():
    try:
        user_repo = UserRepo_postgres()
        user_repo.update_user_data('0', 'full_name', 'vvv')
        assert True
    except Exception as e:
        print(e)
        assert False

def test_get_user():
    try:
        user_repo = UserRepo_postgres()
        user = user_repo.get_user('0')
        print(user.account)
        assert user.email == 'aaa@aaa.com'
    except Exception as e:
        print(e)
        assert False

def remove_user():
    user_repo = UserRepo_postgres()
    user_repo.remove_user('0')