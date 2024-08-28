import allure

from api import requests
from data.user import user_first
from utils.schema import validate_json_schema


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Create User")
def test_create_user(base_url):
    response = requests.post_request(base_url + '/v2/user', json=user_first)
    assert response.status_code == 200
    assert response.json()["type"] == "unknown"
    assert response.json()["message"], "message не может быть пустым"
    validate_json_schema("user/create_user.json", response)


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Create User with array")
def test_create_user_with_array(base_url):
    payload = [user_first]
    response = requests.post_request(base_url + '/v2/user/createWithArray', json=payload)
    assert response.status_code == 200
    assert response.json()["type"] == "unknown"
    assert response.json()["message"], "ok"
    validate_json_schema("user/create_user.json", response)


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Create User with list")
def test_create_user_with_list(base_url):
    payload = [user_first]
    response = requests.post_request(base_url + '/v2/user/createWithList', json=payload)
    assert response.status_code == 200
    assert response.json()["type"] == "unknown"
    assert response.json()["message"], "ok"
    validate_json_schema("user/create_user.json", response)


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
    validate_json_schema("user/get_user.json", response)


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Get not found User")
def test_get_not_found_user(base_url):
    response = requests.get_request(base_url + '/v2/user/user55')
    assert response.status_code == 404
    assert response.json()["type"] == "error"
    assert response.json()["message"] == "User not found"
    validate_json_schema("user/user_not_found.json", response)


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Get empty User")
def test_get_empty_user(base_url):
    response = requests.get_request(base_url + '/v2/user/')
    assert response.status_code == 405


