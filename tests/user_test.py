import allure

from api import requests
from data.user import user_first
from utils.schema import validate_json_schema


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Create User")
def test_create_user(base_url):
    response = requests.post_request(base_url + '/user', json=user_first)
    assert response.status_code == 200, "Ожидается статус код 200"
    assert response.json()["type"] == "unknown", "type должен быть unknown"
    assert response.json()["message"], "message не может быть пустым"
    validate_json_schema("user/create_user.json", response)


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Create User with array")
def test_create_user_with_array(base_url):
    payload = [user_first]
    response = requests.post_request(base_url + '/user/createWithArray', json=payload)
    assert response.status_code == 200, "Ожидается статус код 200"
    assert response.json()["type"] == "unknown", "type должен быть unknown"
    assert response.json()["message"], "ok"
    validate_json_schema("user/create_user.json", response)


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Create User with list")
def test_create_user_with_list(base_url):
    payload = [user_first]
    response = requests.post_request(base_url + '/user/createWithList', json=payload)
    assert response.status_code == 200, "Ожидается статус код 200"
    assert response.json()["type"] == "unknown", "type должен быть unknown"
    assert response.json()["message"] == "ok", "message должен быть ok"
    validate_json_schema("user/create_user.json", response)


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Get User")
def test_get_user(base_url):
    response = requests.get_request(base_url + '/user/Andrey')
    assert response.status_code == 200, "Ожидается статус код 200"
    assert response.json()["username"] == "Andrey", "username не совпадает"
    assert response.json()["firstName"] == "Ivanov", "firstName не совпадает"
    assert response.json()["email"] == "test@test.ru", "email не совпадает"
    validate_json_schema("user/get_user.json", response)


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Get not found User")
def test_get_not_found_user(base_url):
    response = requests.get_request(base_url + '/user/user55')
    assert response.status_code == 404, "Ожидается статус код 404"
    assert response.json()["type"] == "error", "type должен быть error"
    assert response.json()["message"] == "User not found", "message должен быть 'User not found'"
    validate_json_schema("user/user_not_found.json", response)


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Get empty User")
def test_get_empty_user(base_url):
    response = requests.get_request(base_url + '/user/')
    assert response.status_code == 405, "Ожидается статус код 405"


