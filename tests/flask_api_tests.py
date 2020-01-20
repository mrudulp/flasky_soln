
from flask_api import FlaskApi

default_user = 'admin1'
default_pwd = 'admin1'
default_phone_no = '1234'
default_firstname = 'm'
default_lastname = 'p'
new_phone_no = '123456709'

def validate_default_values():
    fa = FlaskApi()
    response = fa.get_token(default_user, default_pwd)
    token = response.json()['token']
    response = fa.get_user_info(token, default_user)
    assert response.status_code == 200
    payload = response.json()['payload']
    assert payload['phone'] == default_phone_no
    assert payload['firstname'] == default_firstname
    assert payload['lastname'] == default_lastname

def reset_to_default():
    update_user_info_payload = {'phone':default_phone_no}
    fa = FlaskApi()
    response = fa.get_token(default_user, default_pwd)
    token = response.json()['token']
    response = fa.update_user_info(token, default_user, update_user_info_payload)
    assert response.status_code == 201
    assert response.json()['status'] == "SUCCESS"

def test_get_token_without_valid_credentials():
    user = 'admin123'
    fa = FlaskApi()
    response = fa.get_token(user, default_pwd)
    assert response.status_code != 200

def test_get_token_with_valid_credentials():
    fa = FlaskApi()
    response = fa.get_token(default_user, default_pwd)
    assert response.status_code == 200

def test_get_users_list_without_valid_token():
    fa = FlaskApi()
    token = '1234'
    response = fa.get_users_list(token)
    assert response.status_code != 200

def test_get_users_list_with_valid_token():
    fa = FlaskApi()
    response = fa.get_token(default_user, default_pwd)
    token = response.json()['token']
    response = fa.get_users_list(token)
    assert response.status_code == 200

def test_get_user_info_without_valid_token():
    fa = FlaskApi()
    token = '1234'
    response = fa.get_user_info(token, default_user)
    assert response.status_code != 200

def test_get_user_info_with_other_user_valid_token():
    fa = FlaskApi()
    response = fa.get_token(default_user, default_pwd)
    token = response.json()['token']
    # change user
    user = 'admin'
    response = fa.get_user_info(token, user)
    assert response.status_code != 200

def test_get_user_info_with_valid_token():
    fa = FlaskApi()
    response = fa.get_token(default_user, default_pwd)
    token = response.json()['token']
    response = fa.get_user_info(token, default_user)
    assert response.status_code == 200

def test_update_user_info_without_valid_username():
    update_user_info_payload = {'phone':new_phone_no}
    fa = FlaskApi()
    response = fa.get_token(default_user, default_pwd)
    token = response.json()['token']
    user = 'admin123' # make user name as invalid user name
    response = fa.update_user_info(token, user, update_user_info_payload)
    assert response.status_code != 200

def test_update_user_info_without_valid_token():
    update_user_info_payload = {'phone':new_phone_no}
    fa = FlaskApi()
    token = '1234'
    response = fa.update_user_info(token, default_user, update_user_info_payload)
    assert response.status_code != 200
    validate_default_values()

def test_update_user_info_without_valid_field():
    update_user_info_payload = {'phone1':new_phone_no}
    fa = FlaskApi()
    response = fa.get_token(default_user, default_pwd)
    token = response.json()['token']
    response = fa.update_user_info(token, default_user, update_user_info_payload)
    assert response.status_code != 200

def test_update_user_info_with_valid_parameters():
    update_user_info_payload = {'phone':new_phone_no}
    fa = FlaskApi()
    response = fa.get_token(default_user, default_pwd)
    token = response.json()['token']
    response = fa.update_user_info(token, default_user, update_user_info_payload)
    assert response.status_code == 201
    assert response.json()['status'] == "SUCCESS"
    reset_to_default()
    validate_default_values()
