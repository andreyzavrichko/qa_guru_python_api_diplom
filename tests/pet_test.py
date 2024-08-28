import allure
import pytest

from api import requests
from data.pet import pet_first
from utils.schema import validate_json_schema


@allure.feature("Pet")
@allure.story("Pet")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Find by status")
@pytest.mark.parametrize("status", ["available", "pending", "sold", "null"])
def test_find_by_status(base_url, status):
    params = {"status": status}
    response = requests.get_request(base_url + '/pet/findByStatus', params=params)
    assert response.status_code == 200, "Ожидается статус код 200"
    data = response.json()
    for item in data:
        assert 'id' in item, f"Поле 'id' отсутствует в элементе: {item}"
        assert item['id'], f"Поле 'id' пустое в элементе: {item}"
    validate_json_schema("pet/find_by_status.json", response)


@allure.feature("Pet")
@allure.story("Pet")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Find by pet ID")
def test_find_pet_by_id(base_url, create_pet):
    pet_id = create_pet
    response = requests.get_request(base_url + f'/pet/{pet_id}')
    assert response.status_code == 200, "Ожидается статус код 200"
    assert response.json()["id"] == pet_id, "id не совпадают"
    validate_json_schema("pet/find_by_pet_id.json", response)


@allure.feature("Pet")
@allure.story("Pet")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Create pet")
def test_create_pet(base_url, delete_pet):
    response = requests.post_request(base_url + '/pet', json=pet_first)
    assert response.status_code == 200, "Ожидается статус код 200"
    assert response.json()["id"], "Поле ID не должно быть пустым"
    assert response.json()["name"] == pet_first.get("name")
    assert response.json()["status"] == "available"
    validate_json_schema("pet/pet.json", response)
    delete_pet(response.json()["id"])