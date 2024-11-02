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
