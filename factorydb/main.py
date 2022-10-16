from faker import Faker

from factorydb.generators import generate_employees


def main():
    fake = Faker(['pl-PL'])

    employees = generate_employees(fake)

    for employee in employees:
        print(employee)


if __name__ == "__main__":
    main()
