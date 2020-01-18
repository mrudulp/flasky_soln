# import pytest
from flask_api import FlaskApi

default_user = 'admin1'
default_pwd = 'admin1'
default_phone_no = '1234'
new_phone_no = '123456709'

def test_get_token_without_valid_credentials():
    fa = FlaskApi()
    response = fa.get_token(default_user, default_pwd)
    assert response.status_code != 200

def test_get_token_with_valid_credentials():
    user = 'admin1'
    pwd = 'admin1'
    fa = FlaskApi()
    response = fa.get_token(user, pwd)
    assert response.status_code == 200

def test_get_users_list_without_valid_token():
    fa = FlaskApi()
    token = '1234'
    response = fa.get_users_list(token)
    assert response.status_code != 200

def test_get_users_list_with_valid_token():
    user = 'admin1'
    pwd = 'admin1'
    fa = FlaskApi()
    response = fa.get_token(user, pwd)
    token = response.json()['token']
    response = fa.get_users_list(token)
    assert response.status_code == 200

def test_get_user_info_without_valid_token():
    user = 'admin1'
    fa = FlaskApi()
    token = '1234'
    response = fa.get_user_info(token, user)
    assert response.status_code != 200

def test_get_user_info_with_other_user_valid_token():
    user = 'admin1'
    pwd = 'admin1'
    fa = FlaskApi()
    response = fa.get_token(user, pwd)
    token = response.json()['token']
    # change user
    user = 'admin'
    response = fa.get_user_info(token, user)
    assert response.status_code != 200

def test_get_user_info_with_valid_token():
    user = 'admin1'
    pwd = 'admin1'
    fa = FlaskApi()
    response = fa.get_token(user, pwd)
    token = response.json()['token']
    response = fa.get_user_info(token, user)
    assert response.status_code == 200

def test_update_user_info_without_valid_username():
    update_user_info_payload = {'phone':new_phone_no}
    fa = FlaskApi()
    response = fa.get_token(default_user, default_pwd)
    token = response.json()['token']
    user = 'nonadmin1' # make user name as invalid user name
    response = fa.update_user_info(token, user, update_user_info_payload)
    assert response.status_code != 200

def test_update_user_info_without_valid_token():
    update_user_info_payload = {'phone':new_phone_no}
    fa = FlaskApi()
    token = '1234'
    response = fa.update_user_info(token, default_user, update_user_info_payload)
    assert response.status_code != 200

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
