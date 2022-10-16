from faker import Faker

from factorydb.factories import Employee


def generate_employees(fake: Faker, count=5000):
    for i in range(count):
        yield Employee(fake)
