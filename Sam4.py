class Human:
    def __init__(self, age, name):
        self._age = age
        self._name = name

    def introduce(self):
        print(f"Hi, my name is {self._name}, I am {self.get_age()} years old.")

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

Gleb = Human("23", "Gleb")
Gleb.introduce()

Gleb.set_age("24")
Gleb.set_name("Gleb Nagoev")
Gleb.introduce()
