import json

import allure
from jsonschema.validators import validate

from utils.resource import path


def validate_json_schema(json_schema, response):
    json_file = path(f'schemas/{json_schema}')

    with open(json_file) as file:
        with allure.step('Валидация типов данных.'):
            validate(response.json(), schema=json.loads(file.read()))