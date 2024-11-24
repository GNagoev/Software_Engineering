# Тема 11. Итераторы и генераторы.
Отчет по Теме #11 выполнил:
- Нагоев Глеб Романович
- ИВТ-22-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ | 
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | - | - |
| Задание 7 | - | - |
| Задание 8 | - | - |
| Задание 9 | - | - |
| Задание 10 | - | - |



## Лабораторная работа №1
### Простой итератор, но у него нет гибкой настройки, например его нельзя развернуть. Он работает просто как next(), но нет prev().
```python
numbers = [0, 1, 2, 3, 4, 5]
for item in numbers:
    print(item)
```

### Результат.

![image](https://github.com/user-attachments/assets/b7415ec5-eb54-4edc-b17d-80f296015454)




## Лабораторная работа №2
### Класс итератор с гибкой настройкой и удобными применением.

```python
class CountDown:
    def __init__(self, start):
        self.count = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count -=1
        if self.count < 0:
            raise StopIteration
        return self.count

if __name__== "__main__":
    counter = CountDown(5)
    for i in counter:
        print(i)
```


### Результат.

![image](https://github.com/user-attachments/assets/3dde87a1-b66e-44d6-8769-1b269b96d2b1)






## Лабораторная работа №3
### Генератор списка.



```python
a = [i**2 for i in range(1,5)]

print('a-', a)
for i in a:
    print(i)

print('iter(a) -', iter(a))
for i in a:
    print(i)
```



### Результат.

![image](https://github.com/user-attachments/assets/c7a2be12-ea31-4378-86b8-b16366d55bd3)






## Лабораторная работа №4
### Выражения генераторы.

```python
b = (i**2 for i in range(1,5))
print(b)
print('first')
for i in b:
    print(i)
print('second')

for i in b:
    print(i)
```

### Результат.

![image](https://github.com/user-attachments/assets/44fb4c33-5b77-45c3-8b20-fc0a4a60ae11)







## Лабораторная работа №5
### Такой же счетчик, как и в первом задании, только это генератор и использует yield.

```python
def countdown(count):
    while count>=0:
        yield count
        count -=1

if __name__== '__main__':
    counter = countdown(5)
    for i in counter:
        print(i)
```

### Результат.

![image](https://github.com/user-attachments/assets/9865ab92-ddc5-4a71-9a92-17ec7d3cbdf9)







## Самостоятельная работа №1
### Вас никак не могут оставить числа Фибоначчи, очень уж они вас заинтересовали. Изучив новые возможности Python вы решили реализовать программу, которая считает числа Фибоначчи при помощи итераторов. Расчет начинается с чисел 1 и 1. Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными затратами ресурсов. Для реализации этой функции потребуется обратиться к инструкции yield (Она не сохраняет в оперативной памяти огромную последовательность, а дает возможность “доставать” промежуточные результаты по одному). Результатом решения задачи будет листинг кода и вывод в консоль с числом Фибоначчи от 200.

```python
def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fibonacci_numbers = list(fib(200))
print(fibonacci_numbers[-1])
```

### Результат.

![image](https://github.com/user-attachments/assets/b3772498-c449-43b1-b9cc-77df2a9b14fe)




## Самостоятельная работа №2
### К коду предыдущей задачи добавьте запоминание каждого числа Фибоначчи в файл “fib.txt”, при этом каждое число должно находиться на отдельной строчке. Результатом выполнения задачи будет листинг кода и скриншот получившегося файла.


```python
def fib(n):
    a, b = 1, 1
    with open("fib.txt", "w") as f:
        for _ in range(n):
            f.write(str(a) + "\n")
            yield a
            a, b = b, a + b

fibonacci_numbers = list(fib(200))
print(fibonacci_numbers[-1])
```

### Результат.

![image](https://github.com/user-attachments/assets/1f1100bc-172d-4e2d-9577-77798bcfc194)

![image](https://github.com/user-attachments/assets/d0c8a42e-7113-44e6-9e14-2d808be28532)
