from dataclasses import dataclass

from faker import Faker


@dataclass
class Pet:
    name: str
    status: str


fake = Faker('ru_RU')

pet_first = {
    "name": fake.first_name(),
    "status": "available"
}
