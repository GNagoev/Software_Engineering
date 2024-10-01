from datetime import datetime # импортируем модуль datetime 
from math import sqrt # импортируем функцию sqrt 

def main(**kwargs): # определяем функцию main, она принимает словарь
    for key in kwargs.items(): # цикл forпроходящий по парам ключ-значение в словаре 
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2) # извлекаем значение по ключу, то бишь
        # список из двух элементов и вычисляем квадратный корень суммы
        # квадратов элементов списка 
        print(result) # вывод результата

if __name__ == '__main__': # проверка на то что у нас нужный модуль
    start_time = datetime.now() # замеряем время начала выполнения программы
    main( # вызов функции main, передаем словарь с координатами
        one = [10, 3], # one - имя точки, [10, 3] - ее координаты
        two = [5, 4], # и тд
        three = [15, 13], # и тд
        four = [93, 53], # и тд
        five = [133, 15] # и тд
    )
time_costs = datetime.now() - start_time # замеряем время окончания выполнения программы
print(f"Время выполнения программы - {time_costs}") # вывод времени выполнения программы
