import pytest
from service.auth.auth_service import AuthFactory

@pytest.mark.parametrize('class_name',['Auth_Line', 'Auth_Google'])
def test_auth_factory(class_name):
    try:
        auth_class = AuthFactory.create_auth(class_name)
        auth = auth_class()
        assert auth.__class__.__name__ == class_name
    except Exception as e:
        print(f'Error: {e}')
        assert False

