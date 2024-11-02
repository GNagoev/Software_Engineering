class Tomato:
    states = ['отсутствует', 'цветение', 'зеленый', 'красный']

    def __init__(self, index):
        self._index = index  # Динамическое свойство: индекс помидора
        self._state = self.states[0]  # Динамическое свойство: начальная стадия созревания (отсутствует)

    def grow(self):
        current_index = self.states.index(self._state)
        if current_index < len(self.states) - 1:
            self._state = self.states[current_index + 1]

    def is_ripe(self):
        return self._state == 'красный'
