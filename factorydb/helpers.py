from faker import Faker

from factorydb.factories import Employee


def generate_employees(count=5000):
    fake = Faker(['pl-PL'])

    for i in range(count):
        yield Employee(fake)
