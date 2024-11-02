class Tomato:
    states = ['отсутствует', 'цветение', 'зеленый', 'красный']

    def __init__(self, index):
        self._index = index
        self._state = self.states[0]

    def grow(self):
        current_index = self.states.index(self._state)
        if current_index < len(self.states) - 1:
            self._state = self.states[current_index + 1]

    def is_ripe(self):
        return self._state == 'красный'


class TomatoBush:
    def __init__(self, number_of_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(number_of_tomatoes)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant):
        self.name = name  # Публичное свойство: имя садовника
        self._plant = plant  # Динамическое свойство: куст помидоров

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собрал урожай!")
            self._plant.give_away_all()
        else:
            print("Томаты еще не созрели.")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:\n"
              "1. Сначала поливайте ваши растения.\n"
              "2. После каждого полива проверяйте на зрелость.\n"
              "3. Если плоды созрели, собирайте их.")



Gardener.knowledge_base()

bush = TomatoBush(5)
gardener = Gardener("Глеб", bush)

gardener.work()

gardener.harvest()
gardener.work()
gardener.harvest()

for _ in range(3):
    gardener.work()
gardener.harvest()
