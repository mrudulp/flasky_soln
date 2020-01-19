from flask_api import FlaskApi

class FlaskWrapper:

    # fa = FlaskApi()
    # response = fa.get_token('admin1', 'admin1')
    # token = response.json()['token']
    # print(f"Token Returned is {token}")
    # # token = 'ODg5MDk3NjI0MjI4OTE1MTY2MzczNDA5NzA4Njg2MzA0NzU1Njk='
    def __init__(self):
        self.fa = FlaskApi()

    def __get_token(self, username, password):
        '''
        Get Token for given username
        '''
        try:
            response = self.fa.get_token(username, password)
            if response.status_code == 200:
                return response.json()['token']
            else:
                print(f"Request Failed with status_code :: {response.status_code}")
                return None
        except Exception as e:
            print(f"Exception for token request::{e}")
            return None


    def get_users_list(self, username, password):
        '''
        Get list of Registered Users
        '''
        try:
            token = self.__get_token(username, password)
            if not token:
                return None # we dont need to send further request as token cannot be None
            response = self.fa.get_users_list(token)
            if response.status_code == 200:
                return response.json()['payload']
            else:
                print(f"Request Failed with status_code :: {response.status_code}")
                return None

        except Exception as e:
            print(f"Exception for Get Users List request::{e}")
            return None
    
    def get_user_info(self, username, password):
        '''
        Gets User Info for a given username
        '''
        try:
            token = self.__get_token(username, password)
            response = self.fa.get_user_info(token, username)
            if response.status_code == 200:
                return response.json()['payload']
            else:
                print(f"Request Failed with status_code :: {response.status_code}")
                return None

        except Exception as e:
            print(f"Exception for Get User Info request::{e}")
            return None

    def update_user_info(self, username, password, json_data):
        '''
        Updates User Info for a given  user
        '''
        try:
            token = self.__get_token(username, password)
            response = self.fa.update_user_info(token, username, json_data)
            if response.status_code == 201:
                if response.json()['status'] == 'SUCCESS':
                    return response.json()['message']
            else:
                return None

        except Exception as e:
            print(f"Exception for Update User Info request::{e}")
            return None

if __name__ == "__main__":

    default_user = 'admin1'
    default_pwd = 'admin1'
    default_phone_no = '1234'
    new_phone_no = '123456709'
    update_user_info_payload = {'phone':new_phone_no}
    fw = FlaskWrapper()
    # users_list = fw.get_users_list(user, pwd)
    # response = fw.get_user_info(user, pwd)
    # response = fw.update_user_info(user, pwd, update_user_info_payload)

    update_user_info_payload = {'phone1':new_phone_no}
    fw = FlaskWrapper()
    response = fw.update_user_info(default_user, default_pwd, update_user_info_payload)
    # Validation
    assert response is None
    response = fw.get_user_info(default_user, default_pwd)
    assert type(response) is dict
    assert response['phone'] == default_phone_no
