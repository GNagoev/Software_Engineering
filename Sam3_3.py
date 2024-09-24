number = int(input("Введите число от 0 до 10: "))
if 0 <= number <= 10:
  if number <= 3:
    print("Число в диапазоне от 0 до 3")
  elif number <= 6:
    print("Число в диапазоне от 3 до 6")
  else:
    print("Число в диапазоне от 6 до 10")
else:
  print("ЧИсло больше 10 или меньше 0")
