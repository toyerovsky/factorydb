from faker import Faker

from factorydb.generators import generate_employees, generate_employees_with_elements

import pandas as pd


def main():
    fake = Faker(['pl-PL'])

    employees = list(generate_employees(fake))
    columns = ["id", "name", "date_of_employment", "employment_type", "team"]
    employees_frame = pd.DataFrame.from_records([e.__dict__ for e in employees])
    employees_frame.to_csv('employees.csv', columns=columns, index=False)
    employees_with_elements = list(generate_employees_with_elements(employees))
    pd.DataFrame(data=employees_with_elements).to_csv('elements.csv', index=False)


if __name__ == "__main__":
    main()
