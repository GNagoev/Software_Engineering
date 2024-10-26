class Car:  # Определяем класс Car
    def __init__(self, make, model):  # Определяем метод инициализации (конструктор),он принимает параметры make и model.
        self.make = make  # Сохраняем марку автомобиля в атрибуте make объекта.
        self.model = model  # Сохраняем модель автомобиля в атрибуте model объекта.

my_car = Car("Toyota", "Corolla")  # Создаем экземпляр класса Car с маркой "Toyota" и моделью "Corolla".
