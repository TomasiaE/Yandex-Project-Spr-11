import configuration
import requests
import data
from data import kit_body


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def post_new_client_kit(kit_body, user_token):
    headers_with_token = data.headers.copy()  # делаем копию заголовков
    headers_with_token["Authorization"] = "Bearer " + user_token  # добавляем в заголовки токен
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_A_SET,
                         json=kit_body,
                         headers=headers_with_token)