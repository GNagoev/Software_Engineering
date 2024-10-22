# Тема 7. Работа с файлами (ввод, вывод).
Отчет по Теме #7 выполнил:
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
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.


### Результат.

![image](https://github.com/user-attachments/assets/829758be-520e-4f79-8989-8a19f9494396)






## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readline())
f.close()
```


### Результат.

![image](https://github.com/user-attachments/assets/359e3356-da6b-456c-a642-c4bcbae98b56)






## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().


```python
f = open('input.txt', 'r')
print(f.readlines())
f.close()
```



### Результат.

![image](https://github.com/user-attachments/assets/2a8f2e97-d78d-4d59-9181-fe669a1cdb4a)






## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    print(f.readlines())
```

### Результат.

![image](https://github.com/user-attachments/assets/ff985bac-198d-497c-b3db-5994d72e7e25)






## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    for line in f:
        print(line)
```

### Результат.

![image](https://github.com/user-attachments/assets/a84665cf-3c74-4ef7-9c2b-624a537966a4)



## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```python
with open('input.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
```

### Результат.

![image](https://github.com/user-attachments/assets/b110b701-1f5d-4cb1-9f2f-48f2bc75b42e)


![image](https://github.com/user-attachments/assets/1f771657-a090-4b4a-b8ae-03738e7998bc)



## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.

```python
lines = ['one', 'two', 'three']
with open ('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```

### Результат.

![image](https://github.com/user-attachments/assets/bf734a55-bb41-451d-9859-afdf192ecc1d)

![image](https://github.com/user-attachments/assets/25a77885-db64-485f-a8b9-98c251780dcc)



## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).

```python
import os


def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка{catalog[0]} содержит:')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)


print_docs(r'C:\Users\Глеб\Software_Engineering\pic')
```

### Результат.

![image](https://github.com/user-attachments/assets/d43c54d7-d94c-4b49-86f4-8428ca658a06)


## Лабораторная работа №9
### Документ «input.txt» содержит следующий текст:
Приветствие
Спасибо
Извините
Пожалуйста
До свидания
Ты готов?
Как дела?
С днем рождения!
Удача!
Я тебя люблю.
### Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).


```python
def longest_words(file):
    with open (file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words


print(longest_words('input.txt'))
```

### Результат.

![image](https://github.com/user-attachments/assets/8bf5c901-e22b-4d57-b425-9e18cd3728e9)

![image](https://github.com/user-attachments/assets/fb97c2da-8878-4790-98e1-4e28acbb4dad)

![image](https://github.com/user-attachments/assets/3cc4c9ea-bc15-40ac-ba83-0854b5e0d83d)


## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими
столбцами:
• № - номер по порядку (от 1 до 300);
• Секунда – текущая секунда на вашем ПК;
• Микросекунда – текущая миллисекунда на часах.
### Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда ', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second,
                         datetime.datetime.now().microsecond])
        time.sleep(0.01)
```

### Результат.

![image](https://github.com/user-attachments/assets/2cccc32a-6270-4f8e-8ad3-e51c4ed20e12)

![image](https://github.com/user-attachments/assets/5db713ad-ff60-4c59-a450-5651f059cf47)



## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

```python
from collections import Counter
import re


def analyze_text_file(directory):
    try:
        with open(directory, 'r', encoding='utf-8') as file:
            text = file.read()
        words = re.findall(r'\b\w+\b', text.lower())
        word_count = len(words)
        word_frequency = Counter(words)
        most_common_word, most_common_count = word_frequency.most_common(1)[0]
        print(f"Количество слов в файле: {word_count}")
        print(f"Самое часто встречающееся слово: '{most_common_word}' (встречается {most_common_count} раз)")

analyze_text_file(r'C:\Users\Глеб\PycharmProjects\lab_1\input.txt')
```

### Результат.

![image](https://github.com/user-attachments/assets/4f4fd71d-ba7d-4d7d-be78-397b571e71fa)

![image](https://github.com/user-attachments/assets/ec299c3a-8169-40b2-a196-3f62677371b6)



## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
Текст в файле:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.

Ожидаемый результат:
Input file contains:
108 letters
20 words
4 lines
```python
def analyze_text(directory):
    with open(directory, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    total_letters = 0
    total_words = 0
    total_lines = len(lines)
    for line in lines:
        total_letters += sum(c.isalpha() and c.isascii() for c in line)
        total_words += len(line.split())
    print(f"Количество букв латинского алфавита: {total_letters}")
    print(f"Количество слов: {total_words}")
    print(f"Количество строк: {total_lines}")

analyze_text(r'C:\Users\Глеб\PycharmProjects\lab_1\input.txt')
```

### Результат.

![image](https://github.com/user-attachments/assets/f32e60dc-e180-4700-ba75-97edfe6dc710)

![image](https://github.com/user-attachments/assets/77a36dea-894b-4faf-9d6c-e0678c547516)


## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
Запрещенные слова:
hello email python the exam wor is
• Предложение для проверки:
Hello, world! Python IS the programming language of thE future. My
EMAIL is....
PYTHON is awesome!!!!
• Ожидаемый результат:
*****, ***ld! ****** ** *** programming language of *** future. My
***** **....
****** ** awesome!!!!

```python
import re

def load_banned_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]
def replace_banned_words(sentence, banned_words):
    for word in banned_words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        sentence = pattern.sub('*' * len(word), sentence)
    return sentence
def main():
    banned_words = load_banned_words('input.txt')
    sentence = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"
    result = replace_banned_words(sentence, banned_words)
    print("Результат:", result)
if __name__ == "__main__":
    main()
```

### Результат.

![image](https://github.com/user-attachments/assets/70310ae7-4e41-4c8c-a6e0-c9c8d2f3e66e)

![image](https://github.com/user-attachments/assets/064db146-13c4-4733-af45-d5966c782cc1)



## Самостоятельная работа №5
### Дан текстовый файл. Замени все заглавные буквы на строчные.
```python
def read_and_convert(directory):
    with open(directory, 'r', encoding='utf-8') as file:
        content = file.read()
    modified_content = content.lower()
    print(modified_content)

read_and_convert(r'C:\Users\Глеб\PycharmProjects\lab_1\input.txt')
```

### Результат.


![image](https://github.com/user-attachments/assets/d8599b3a-d124-47d2-94d9-95cf3be82a17)

![image](https://github.com/user-attachments/assets/f1690a00-1d60-44a3-a43b-7994cebad40e)

