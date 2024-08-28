import random
from dataclasses import dataclass

from faker import Faker


@dataclass
class User:
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int


fake = Faker('ru_RU')

user_first = {
    "username": fake.user_name(),
    "firstName": fake.first_name(),
    "lastName": fake.last_name(),
    "email": fake.email(),
    "password": fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True),
    "phone": fake.phone_number(),
    "userStatus": random.choice([0, 1])
}
