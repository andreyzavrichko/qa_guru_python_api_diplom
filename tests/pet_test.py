import json

import allure
import pytest

from api import requests
from utils.resource import path

from jsonschema.validators import validate


@allure.feature("Pet")
@allure.story("Pet")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Find by status")
@pytest.mark.parametrize("status", ["available", "pending", "sold", "null"])
def test_find_by_status(base_url, status):
    params = {"status": status}
    response = requests.get_request(base_url + '/v2/pet/findByStatus', params=params)
    assert response.status_code == 200
    data = response.json()
    for item in data:
        assert 'id' in item, f"Поле 'id' отсутствует в элементе: {item}"
        assert item['id'], f"Поле 'id' пустое в элементе: {item}"

    schema = path('pet/find_by_status.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))


@allure.feature("Pet")
@allure.story("Pet")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Find by pet ID")
def test_find_pet_by_id(base_url):
    response = requests.get_request(base_url + '/v2/pet/9223372036854775000')
    assert response.status_code == 200
    assert response.json()["id"] == 9223372036854775000
    assert response.json()["name"] == "doggie"

    schema = path('pet/find_by_pet_id.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))


@allure.feature("Pet")
@allure.story("Pet")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Create pet")
def test_create_pet(base_url):
    payload = {
        "name": "pet",
        "status": "available"
    }
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    response = requests.post_request(base_url + '/v2/pet', headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["id"], "Поле ID не должно быть пустым"
    assert response.json()["name"] == "pet"
    assert response.json()["status"] == "available"

    schema = path('pet/pet.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))
