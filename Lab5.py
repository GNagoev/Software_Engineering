class Shape:  # Определяем общий класс Shape
    def area(self):  # Определяем метод для расчета площади (будет переопределен в дочерних классах)
        pass

class Rectangle(Shape):  # Определяем класс Rectangle, наследующий от Shape
    def __init__(self, width, height):  # Метод инициализации, принимающий ширину и высоту
        self.width = width  # Сохраняем ширину
        self.height = height  # Сохраняем высоту

    def area(self):  # Переопределяем метод area для расчета площади прямоугольника
        return self.width * self.height  # Возвращаем площадь

class Circle(Shape):  # Определяем класс Circle, наследующий от Shape
    def __init__(self, radius):  # Метод инициализации, принимающий радиус
        self.radius = radius  # Сохраняем радиус

    def area(self):  # Переопределяем метод area для расчета площади круга
        return 3.14 * self.radius * self.radius  # Возвращаем площадь

# Создаем массив с фигурами
shapes = [Rectangle(5, 4), Circle(3)]  # Добавляем экземпляры прямоугольника и круга

# Выводим площади фигур
for shape in shapes:  # Проходим по каждой фигуре в массиве
    print(f"The area is: {shape.area()}")  # Вызываем метод area и выводим площадь
