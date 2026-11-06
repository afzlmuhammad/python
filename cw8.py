class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
        
class Employee(Person):
    def __init__(self, name, age, employee_id):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}")
        
        
class PartTime(Person):
    def __init__(self, name, age, working_hours):
        Person.__init__(self, name, age)
        self.working_hours = working_hours
        
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Working hours: {self.working_hours}")
        
class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.working_hours = working_hours
        self.project_name = project_name
        
    def show_details(self):
        print(f"Name = {self.name}, Age = {self.age}, Employee ID = {self.employee_id}, Working Hours = {self.working_hours}, Project = {self.project_name}")
        
        
p = Person("Asha", 30)
e = Employee("Ravi", 28, "E101")
pt = PartTime("Meera", 22, 20.5)
c = Consultant("Arun", 35, "E202", 15.0, "Website Redesign")

p.show_details()
e.show_details()
pt.show_details()
c.show_details()
        
        
        
        