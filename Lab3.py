class Car:  # Определяем класс Car
    def __init__(self, make, model):  # Определяем метод инициализации (конструктор), он принимает параметры make и model.
        self.make = make  # Сохраняем марку автомобиля в атрибуте make объекта.
        self.model = model  # Сохраняем модель автомобиля в атрибуте model объекта.

    def drive(self):  # Определяем метод drive, который описывает действие вождения автомобиля.
        print(f"Driving the {self.make} {self.model}")  # Выводим сообщение о том, что мы за рулем автомобиля, с указанием его марки и модели.

my_car = Car("Toyota", "Corolla")  # Создаем экземпляр класса Car с маркой "Toyota" и моделью "Corolla".
my_car.drive()  # Вызываем метод drive у экземпляра my_car, чтобы вывести сообщение о вождении.

class ElectricCar(Car):  # Определяем класс ElectricCar, который наследуется от класса Car.
    def __init__(self, make, model, battery_capacity):  # Определяем метод инициализации, который принимает параметры make, model и battery_capacity.
        super().__init__(make, model)  # Вызываем метод инициализации родительского класса Car.
        self.battery_capacity = battery_capacity  # Сохраняем емкость батареи в атрибуте battery_capacity объекта.

    def charge(self):  # Определяем метод charge, который описывает действие зарядки электромобиля.
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")  # Выводим сообщение о зарядке автомобиля с указанием его марки, модели и емкости батареи.

my_electric_car = ElectricCar("Tesla", "Model S", 75)  # Создаем экземпляр класса ElectricCar с маркой "Tesla", моделью "Model S" и емкостью батареи 75 kWh.
my_electric_car.drive()  # Вызываем метод drive у экземпляра my_electric_car, чтобы вывести сообщение о вождении.
my_electric_car.charge()  # Вызываем метод charge у экземпляра my_electric_car, чтобы вывести сообщение о зарядке.
