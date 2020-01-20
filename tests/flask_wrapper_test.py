from flask_wrapper import FlaskWrapper

default_user = 'admin1'
default_pwd = 'admin1'
default_phone_no = '1234'
new_phone_no = '123456709'

def validate_default_phone():
    fw = FlaskWrapper()
    response = fw.get_user_info(default_user, default_pwd)
    assert type(response) is dict
    assert response['phone'] == default_phone_no

def reset_to_default():
    fw = FlaskWrapper()
    update_user_info_payload = {'phone':default_phone_no}
    response = fw.update_user_info(default_user, default_pwd, update_user_info_payload)
    assert response == 'Updated'

def test_get_users_list_without_valid_credentials():
    '''
    Test User list is not returned when invalid credentials are provided
    '''
    user = 'admin123'
    fw = FlaskWrapper()
    response = fw.get_users_list(user, default_pwd)
    assert response is None

def test_get_users_list_with_valid_credentials():
    '''
    Test User list is received when valid credentials are provided
    '''
    fw = FlaskWrapper()
    response = fw.get_users_list(default_user, default_pwd)
    assert type(response) is list

def test_get_user_info_without_valid_credentials():
    '''
    Test User Info is not returned when invalid credentials are provided
    '''
    user = 'admin123'
    fw = FlaskWrapper()
    response = fw.get_user_info(user, default_pwd)
    assert response is None

def test_get_user_info_with_valid_credentials():
    '''
    Test User Info is returned when valid credentials are provided
    '''
    fw = FlaskWrapper()
    response = fw.get_user_info(default_user, default_pwd)
    assert type(response) is dict
    keys = response.keys()
    assert "firstname" in keys
    assert "lastname" in keys
    assert "phone" in keys

def test_update_user_info_without_valid_credentials():
    '''
    Test User Info is not updated when invalid credentials are given
    '''
    user = 'nonadmin'
    update_user_info_payload = {'phone': new_phone_no}
    fw = FlaskWrapper()
    response = fw.update_user_info(user, default_pwd, update_user_info_payload)
    assert response is None

def test_update_user_info_without_valid_field():
    '''
    Test User Info is not updated when invalid field is provided
    '''
    update_user_info_payload = {'phone1':'abc'}
    fw = FlaskWrapper()
    response = fw.update_user_info(default_user, default_pwd, update_user_info_payload)
    # Validation
    assert response is None
    validate_default_phone()

def test_update_user_info_with_valid_parameters():
    '''
    Test User Info is updated when valid parameters/field is sent to server
    '''
    update_user_info_payload = {'phone':new_phone_no}
    fw = FlaskWrapper()
    response = fw.update_user_info(default_user, default_pwd, update_user_info_payload)
    # Verification
    assert response == 'Updated'
    response = fw.get_user_info(default_user, default_pwd)
    assert type(response) is dict
    assert response['phone'] == new_phone_no
    # Reset to original phone number
    reset_to_default()
    validate_default_phone()

