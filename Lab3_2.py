number = int(input("Введите значение переменной: "))

if number < 0:
  print("Переменная меньше 0")
elif 0 < number < 10:
  print("Переменная больше 0 и меньше 10")
else:
  print("Переменная больше 10")
