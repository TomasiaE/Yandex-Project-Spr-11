import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body)
user_token = post_new_user(data.user_body)


def post_new_client_kit(kit_body, user_token):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_A_SET,
                         json=data.kit_body,
                         headers=data.headers)

response = post_new_client_kit(data.kit_body,user_token)