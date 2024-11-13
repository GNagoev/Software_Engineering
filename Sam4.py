import time

# Декоратор для фиксирования времени выполнения функции
class TimerDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # Засекаем время начала выполнения
        start_time = time.time()

        # Выполняем саму функцию
        result = self.func(*args, **kwargs)

        # Засекаем время после выполнения
        end_time = time.time()

        # Выводим время выполнения
        print(f"Функция {self.func.__name__} выполнена за {end_time - start_time:.4f} секунд.")

        return result

# Первая функция, которая будет "спать" некоторое время
@TimerDecorator
def do_heavy_computation(seconds):
    print("Начинаю тяжелые вычисления...")
    time.sleep(seconds)
    print("Тяжелые вычисления завершены.")

# Вторая функция, которая выполняет быструю задачу
@TimerDecorator
def quick_task():
    print("Выполняю быструю задачу...")
    time.sleep(0.5)
    print("Задача завершена.")

# Пример выполнения
if __name__ == "__main__":
    do_heavy_computation(3)  # Имитируем тяжелые вычисления с 3-секундной задержкой
    quick_task()  # Быстрая задача с 0.5-секундной задержкой
