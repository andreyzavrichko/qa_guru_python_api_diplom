import json

import allure

from api import requests
from utils.resource import path

from jsonschema.validators import validate


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Create User")
def test_create_user(base_url):
    payload = {
        "username": "Andrey",
        "firstName": "Ivanov",
        "lastName": "string",
        "email": "test@test.ru",
        "password": "PassW0rd$",
        "phone": "11111111",
        "userStatus": 1
    }
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    response = requests.post_request(base_url + '/v2/user', headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["type"] == "unknown"
    assert response.json()["message"], "message не может быть пустым"

    schema = path('user/create_user.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Create User with array")
def test_create_user_with_array(base_url):
    payload = [
        {
            "username": "Andrey",
            "firstName": "Ivanov",
            "lastName": "string",
            "email": "test@test.ru",
            "password": "PassW0rd$",
            "phone": "11111111",
            "userStatus": 1
        }
    ]
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    response = requests.post_request(base_url + '/v2/user/createWithArray', headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["type"] == "unknown"
    assert response.json()["message"], "ok"

    schema = path('user/create_user.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Create User with list")
def test_create_user_with_list(base_url):
    payload = [
        {
            "username": "Andrey",
            "firstName": "Ivanov",
            "lastName": "string",
            "email": "test@test.ru",
            "password": "PassW0rd$",
            "phone": "11111111",
            "userStatus": 1
        }
    ]
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    response = requests.post_request(base_url + '/v2/user/createWithList', headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["type"] == "unknown"
    assert response.json()["message"], "ok"

    schema = path('user/create_user.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Get User")
def test_get_user(base_url):
    response = requests.get_request(base_url + '/v2/user/Andrey')
    assert response.status_code == 200
    assert response.json()["username"] == "Andrey"
    assert response.json()["firstName"] == "Ivanov"
    assert response.json()["email"] == "test@test.ru"

    schema = path('user/get_user.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Get not found User")
def test_get_not_found_user(base_url):
    response = requests.get_request(base_url + '/v2/user/user55')
    assert response.status_code == 404
    assert response.json()["type"] == "error"
    assert response.json()["message"] == "User not found"

    schema = path('user/user_not_found.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Get empty User")
def test_get_empty_user(base_url):
    response = requests.get_request(base_url + '/v2/user/')
    assert response.status_code == 405
