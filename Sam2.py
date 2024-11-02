    def grow(self):
        """Переводит томат на следующую стадию созревания."""
        current_index = self.states.index(self._state)
        if current_index < len(self.states) - 1:
            self._state = self.states[current_index + 1]

    def is_ripe(self):
        """Проверяет, что томат созрел."""
        return self._state == 'красный'

