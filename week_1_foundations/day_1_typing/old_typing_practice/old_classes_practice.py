# Implement some classes with type hints


class Person:
    def __init__(self, name: str, age: int, job: None | str) -> None:
        self.name = name
        self.age = age
        self.job = job

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def work(self) -> str:
        if self.job:
            return f"I work as a {self.job}."
        return "I am currently in between jobs."

class Company:
    def __init__(self, name: str, employees: list[Person]) -> None:
        self.name = name
        self.employees = employees

    def add_employee(self, person: Person) -> None:
        print(f"Adding employee: {person.name}")
        self.employees.append(person)

    def list_employees(self) -> list[str]:
        return [employee.name for employee in self.employees]

if __name__ == "__main__":
    alice = Person("Alice", 30, "Engineer")
    bob = Person("Bob", 25, None)

    print(alice.greet())
    print(alice.work())
    print(bob.greet())
    print(bob.work())

    company = Company("TechCorp", [alice])
    company.add_employee(bob)
    print(f"Employees at {company.name}: {', '.join(company.list_employees())}")
