import random
from dataclasses import dataclass

from faker import Faker


@dataclass
class Order:
    petId: int
    quantity: int
    shipDate: str
    status: str
    complete: bool


fake = Faker('ru_RU')

order_first = {
    "petId": random.randint(1, 100000),
    "quantity": random.randint(1, 10),
    "shipDate": fake.iso8601(tzinfo=None),
    "status": random.choice(["placed", "approved", "delivered"]),
    "complete": random.choice([True, False])
}
