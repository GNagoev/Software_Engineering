string = "Привет, мир!"
value = input()
for i in string:
  if i == value:
    index = string.find(value)
    print(f"Буква '{value}'есть в строке под {index} индексом")
    break

else:
  print(f"Буквы '{value}'нет указанной строке")