import requests as req
# from requests.auth import HTTPBasicAuth

class FlaskApi:
    """
    Class offering apis to flask application
    Does not handle responses or exceptions but lets subsequent classes to handle according to their needs.
    """
    base_url = 'http://localhost:8080/'
    def get_token(self, username, password):
        token_endpoint = f'{FlaskApi.base_url}api/auth/token'
        # basicAuth = HTTPBasicAuth(username, password)
        return req.get(token_endpoint, auth=(username, password))
    
    def get_users_list(self, token):
        user_list_endpoint = f'{FlaskApi.base_url}api/users'
        headers = {'Content-Type': 'application/json', 'Token':token}
        return req.get(user_list_endpoint, headers=headers)
    
    def get_user_info(self, token, username):
        user_info_endpoint = f'{FlaskApi.base_url}api/users/{username}'
        headers = {'Content-Type': 'application/json', 'Token':token}
        return req.get(user_info_endpoint, headers=headers)
    
    def update_user_info(self, token, username, json_data):
        update_user_info_endpoint = f'{FlaskApi.base_url}api/users/{username}'
        headers = {'Content-Type': 'application/json', 'Token':token}
        return req.put(update_user_info_endpoint, json=json_data, headers=headers)

if __name__ == "__main__":

    user = 'admin1'
    pwd = 'admin1'
    update_user_info_payload = {'phone':'12345678'}
    fa = FlaskApi()
    response = fa.get_token(user, pwd)
    token = response.json()['token']
    response = fa.update_user_info(token, user, update_user_info_payload)
    # fa = FlaskApi()
    # response = fa.get_token('admin1', 'admin1')
    # token = response.json()['token']
    # print(f"Token Returned is {token}")
    # # token = 'ODg5MDk3NjI0MjI4OTE1MTY2MzczNDA5NzA4Njg2MzA0NzU1Njk='
    # response = fa.get_users_list(token)
    # users = response.json()['payload']
    # print(f"Users:{users}")
    # response = fa.get_user_info(token, users[0])
    # user_info = response.json()['payload']
    # print(f"User Info:{user_info}")
    # update_user_info_payload = {'phone':'1234567'}
    # response = fa.update_user_info(token, users[0], update_user_info_payload)
    # print(f"update Response f{response.json()}")
    # response = fa.get_user_info(token, users[0])
    # update_info = response.json()['payload']
    # print(f"Updated Info::{update_info}")