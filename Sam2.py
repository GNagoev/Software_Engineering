class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def introduce(self):
        print((f"Hi, my name is {self.name}, i am {self.age} years old."))

Gleb = Human("23", "Gleb")
Gleb.introduce()
