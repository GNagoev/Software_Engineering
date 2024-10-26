class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def introduce(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old.")

Gleb = Human("23", "Gleb")
Gleb.introduce()

class Student(Human):
    def __init__(self, age, name, student_id):
        super().__init__(age, name)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying with student ID {self.student_id}.")

student_gleb = Student("23", "Gleb", "S12345")
student_gleb.introduce()
student_gleb.study()
