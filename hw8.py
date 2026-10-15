class Employee:
    def __init__(self, name, role, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.role = role
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")

class Trainer(Employee):
    def __init__(self, name, role, specialization, **kwargs):
        super().__init__(name=name, role=role, **kwargs)
        self.specialization = specialization
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Specialization: {self.specialization}")
        
class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style, **kwargs):
        super().__init__(name=name, role=role, **kwargs)
        self.yoga_style = yoga_style

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Yoga Style: {self.yoga_style}")
        
class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        super().__init__(name=name, role=role,
                         specialization=specialization,
                         yoga_style=yoga_style)
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Specialization: {self.specialization}")
        print(f"Yoga Style: {self.yoga_style}")

employee = Employee("Anita Roy", "Front Desk Manager")
trainer = Trainer("Rahul Menon", "Personal Trainer", "Strength Training")
yoga_instructor = YogaInstructor("Meera Nair", "Yoga Instructor", "Hatha Yoga")
multi_trainer = MultiTrainer("Arjun Das", "Senior Trainer",
                             "Cardio & HIIT", "Vinyasa Yoga")

for staff in (employee, trainer, yoga_instructor, multi_trainer):
    staff.display()
    print("-" * 30)