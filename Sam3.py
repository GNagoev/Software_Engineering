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
