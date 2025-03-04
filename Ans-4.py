# Base class 1: Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        return f"Name: {self.name}, Age: {self.age}"

# Base class 2: Employee
class Employee:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        return f"Employee ID: {self.employee_id}, Salary: ₹{self.salary}"

# Derived class: Manager (inherits from both Person and Employee)
class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, salary, department):
        # Initialize both base classes
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, salary)
        self.department = department

    def display_manager_info(self):
        return (f"{self.display_person_info()}, {self.display_employee_info()}, "
                f"Department: {self.department}")

# Example usage
manager = Manager("Rahul Sharma", 35, "MGR101", 80000, "IT")

print(manager.display_manager_info())