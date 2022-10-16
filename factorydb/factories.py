from collections import OrderedDict
from datetime import datetime, timedelta

from faker import Faker

import numpy as np

NOW = datetime.now()
THIRTY_YEARS_AGO = NOW - timedelta(days=30*365)

types_of_employment = OrderedDict([("Pełen etat", 0.5), ("Pół etatu", 0.3), ("Zatrudnienie na godziny", 0.2), ])
teams = ('Czerwony', 'Niebieski', 'Zielony', 'Czarny', 'Biały')


class Employee(object):
    def __init__(self, fake: Faker):
        self.id = fake.random_int()
        self.name = fake.name()
        self.date_of_employment = fake.date_between_dates(THIRTY_YEARS_AGO, NOW)
        self.employment_type = fake.random_choices(elements=types_of_employment, length=1)[0]
        self.team = fake.random_choices(elements=teams, length=1)[0]

    def __str__(self):
        return f"<{self.name}> ({self.id}) zespół <{self.team}> zatrudniony na <{self.employment_type}>"


class Element(object):
    def __init__(self):
        self.id = id(self)
        self.step_1 = np.random.gamma(shape=3, scale=1, size=1000)
        self.step_2 = np.random.random(size=1000)
        self.step_3 = np.random.exponential(scale=1, size=1000)

