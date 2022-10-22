from collections import OrderedDict
from datetime import datetime, timedelta

from faker import Faker

import numpy as np

from factorydb.generators import generate_elements

NOW = datetime.now()
THIRTY_YEARS_AGO = NOW - timedelta(days=30*365)

types_of_employment = OrderedDict([("Pełen etat", 0.5), ("Pół etatu", 0.3), ("Zatrudnienie na godziny", 0.2), ])
teams = ('Czerwony', 'Niebieski', 'Zielony', 'Czarny', 'Biały')

number_of_elements = {
    "Pełen etat": (500, 1000),
    "Pół etatu": (100, 500),
    "Zatrudnienie na godziny": (1, 1000)
}


class Employee(object):
    def __init__(self, fake: Faker):
        self.id = fake.random_int()
        self.name = fake.name()
        self.date_of_employment = fake.date_between_dates(THIRTY_YEARS_AGO, NOW)
        self.employment_type = fake.random_choices(elements=types_of_employment, length=1)[0]
        self.team = fake.random_choices(elements=teams, length=1)[0]

        lower_bound, upper_bound = number_of_elements[self.employment_type]
        element_count = fake.random_int(min=lower_bound, max=upper_bound)
        self.elements = list(generate_elements(element_count))


class Element(object):
    def __init__(self):
        self.id = id(self)
        self.step_1 = np.random.gamma(shape=3, scale=1, size=1)[0]
        self.step_2 = np.random.random(size=1)[0]
        self.step_3 = np.random.exponential(scale=1, size=1)[0]