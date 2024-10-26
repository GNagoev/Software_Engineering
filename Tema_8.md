# Тема 8. Введение в ООП.
Отчет по Теме #8 выполнил:
- Нагоев Глеб Романович
- ИВТ-22-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ | 
| Задание 1 | + | + |
| Задание 2 | + | - |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + | - |
| Задание 7 | + | - |
| Задание 8 | + | - |
| Задание 9 | + | - |
| Задание 10 | + | - |



## Лабораторная работа №1
### Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.


```python
class Car:  # Определяем класс Car
    def __init__(self, make, model):  # Определяем метод инициализации (конструктор),он принимает параметры make и model.
        self.make = make  # Сохраняем марку автомобиля в атрибуте make объекта.
        self.model = model  # Сохраняем модель автомобиля в атрибуте model объекта.

my_car = Car("Toyota", "Corolla")  # Создаем экземпляр класса Car с маркой "Toyota" и моделью "Corolla".
```

### Результат.

![image](https://github.com/user-attachments/assets/6545d9ef-fb70-4502-a028-f6e7d30ef53a)




## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:  # Определяем класс Car
    def __init__(self, make, model):  # Определяем метод инициализации (конструктор),он принимает параметры make и model.
        self.make = make  # Сохраняем марку автомобиля в атрибуте make объекта.
        self.model = model  # Сохраняем модель автомобиля в атрибуте model объекта.

    def drive(self):  # Определяем метод drive, который описывает действие вождения автомобиля.
        print(f"Driving the {self.make} {self.model}")  # Выводим сообщение о том, что мы за рулем автомобился, с указанием его марки и модели.

my_car = Car("Toyota", "Corolla")  # Создаем экземпляр класса Car с маркой "Toyota" и моделью "Corolla".
my_car.drive()  # Вызываем метод drive у экземпляра my_car, чтобы вывести сообщение о вождении.
```


### Результат.

![image](https://github.com/user-attachments/assets/7bd5e196-d0ae-4247-9d53-13a2d72cd015)







## Лабораторная работа №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.


```python
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
```



### Результат.

![image](https://github.com/user-attachments/assets/af958559-2d98-4166-8817-966755f8e1ce)







## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:  # Определяем класс Car
    def __init__(self, make, model):  # Определяем метод инициализации (конструктор), он принимает параметры make и model.
        self._make = make  # Сохраняем марку автомобиля в защищенном атрибуте make объекта.
        self.__model = model  # Сохраняем модель автомобиля в приватном атрибуте model объекта.

    def drive(self):  # Определяем метод drive, который описывает действие вождения автомобиля.
        print(f"Driving the {self._make} {self.__model}")  # Выводим сообщение о том, что мы за рулем автомобиля, с указанием его марки и модели.

my_car = Car("Toyota", "Corolla")  # Создаем экземпляр класса Car с маркой "Toyota" и моделью "Corolla".
print(my_car._make) # Доступ к защищенному атрибуту.
my_car.drive()  # Вызываем метод drive у экземпляра my_car, чтобы вывести сообщение о вождении.
```

### Результат.

![image](https://github.com/user-attachments/assets/ca8851a6-ac84-465c-97e3-917423687970)







## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
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
```

### Результат.

![image](https://github.com/user-attachments/assets/788dd383-2417-4d9f-877f-c8cf8d7ccd11)






## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Human:
    def __init__(self, age, sex):
        self.age = age
        self.sex = sex

Gleb = Human("23", "Male")
```

### Результат.

![image](https://github.com/user-attachments/assets/bad8cb0a-8c9d-460c-a7e2-4ec2cbf9f551)




## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def introduce(self):
        print((f"Hi, my name is {self.name}, i am {self.age} years old."))

Gleb = Human("23", "Gleb")
Gleb.introduce()
```

### Результат.


![image](https://github.com/user-attachments/assets/7400f7ff-db20-42a2-9477-69f3fd3f58fa)



## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def introduce(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old.")

Gleb = Human("23", "Gleb")
Gleb.introduce()

class Student(Human):
    def __init__(self, age, name, student_id):
        super().__init__(age, name)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying with student ID {self.student_id}.")

student_gleb = Student("23", "Gleb", "S12345")
student_gleb.introduce()
student_gleb.study()
```

### Результат.

![image](https://github.com/user-attachments/assets/e32bfc59-e418-4800-b7ef-83bfa39e9227)



## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Human:
    def __init__(self, age, name):
        self._age = age
        self._name = name

    def introduce(self):
        print(f"Hi, my name is {self._name}, I am {self.get_age()} years old.")

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

Gleb = Human("23", "Gleb")
Gleb.introduce()

Gleb.set_age("24")
Gleb.set_name("Gleb Nagoev")
Gleb.introduce()
```

### Результат.

![image](https://github.com/user-attachments/assets/38de1520-10f7-4d3e-b901-70d4cd1c6692)




## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def introduce(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old.")

class Student(Human):
    def __init__(self, age, name, student_id):
        super().__init__(age, name)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying with student ID {self.student_id}.")

class Teacher(Human):
    def __init__(self, age, name, subject):
        super().__init__(age, name)
        self.subject = subject

    def introduce(self):
        print(f"Hello, I am {self.name}, I teach {self.subject} and I am {self.age} years old.")

people = [
    Student("23", "Gleb", "S12345"),
    Teacher("30", "Alice", "Mathematics")
]

for person in people:
    person.introduce()

for person in people:
    if isinstance(person, Student):
        person.study()
```

### Результат.


![image](https://github.com/user-attachments/assets/fb81a0a8-bd03-47bd-8897-ef43b50e2d2f)


