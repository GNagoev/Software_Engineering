numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
value = int(input("Введите значение переменной: "))
if value in numbers:
  print("Переменная есть в массиве")
  if value % 2 == 0:
    print("Переменная четная")
  else:
    print("Переменная нечетная")
else:
  print("Переменной нет в массиве")
