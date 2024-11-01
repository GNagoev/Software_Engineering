class Gleb:
    __slots__ = ['name']

    def __init__(self, name):
        if name == 'Глеб':
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, а Глеб"


person1 = Gleb('Иван')
person2 = Gleb('Глеб')
print(person1.name)
print(person2.name)

person2.surname = 'Нагоев'
