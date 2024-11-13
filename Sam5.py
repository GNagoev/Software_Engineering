# Создание собственного исключения
class InvalidDataError(Exception):
    # Исключение, возникающее при неверных данных

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# Функция для проверки типа данных
def process_data(data):
    # Функция, которая обрабатывает данные. Если данные неверные, вызывает исключение
    if not isinstance(data, str):
        raise InvalidDataError("Ожидалась строка, получен другой тип данных.")
    print(f"Данные {data} успешно обработаны!")


# Функция для проверки возраста
def check_age(age):
    # Функция, которая проверяет возраст пользователя. Если возраст отрицательный, вызывает исключение
    if age < 0:
        raise InvalidDataError("Возраст не может быть отрицательным!")
    print(f"Возраст {age} лет успешно принят.")


# Шаг 2: Пример выполнения программы
if __name__ == "__main__":
    # Пример 1: Передача некорректного типа данных
    try:
        process_data(123)  # Ошибка, потому что передан не тип str
    except InvalidDataError as e:
        print(f"Ошибка: {e}")

    # Пример 2: Проверка возраста с неверным значением
    try:
        check_age(-5)  # Ошибка, потому что возраст отрицательный
    except InvalidDataError as e:
        print(f"Ошибка: {e}")

    # Пример 3: Верный случай
    try:
        process_data("Hello, World!")
        check_age(25)
    except InvalidDataError as e:
        print(f"Ошибка: {e}")
