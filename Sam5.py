class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def introduce(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old.")

class Student(Human):
    def __init__(self, age, name, student_id):
        super().__init__(age, name)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying with student ID {self.student_id}.")

class Teacher(Human):
    def __init__(self, age, name, subject):
        super().__init__(age, name)
        self.subject = subject

    def introduce(self):
        print(f"Hello, I am {self.name}, I teach {self.subject} and I am {self.age} years old.")

people = [
    Student("23", "Gleb", "S12345"),
    Teacher("30", "Alice", "Mathematics")
]

for person in people:
    person.introduce()

for person in people:
    if isinstance(person, Student):
        person.study()
