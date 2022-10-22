from faker import Faker



def generate_employees(fake: Faker, count=5000):
    from factorydb.factories import Employee

    for i in range(count):
        yield Employee(fake)


def generate_elements(count):
    from factorydb.factories import Element

    for i in range(count):
        yield Element()


def generate_employees_with_elements(employees):
    for employee in employees:
        for element in employee.elements:
            yield {
                "Item number": f"{element.id}-{employee.id}",
                "Step 1": element.step_1,
                "Step 2": element.step_2,
                "Step 3": element.step_3,
                "Employee id": employee.id
            }

