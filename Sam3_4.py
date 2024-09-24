sentence = input()
print("Длина:", len(sentence))
print("В нижнем регистре:", sentence.lower())
Final_sentence = sentence.lower()
vowels = "aeiou"
vowel_count = 0
for char in Final_sentence:
  if char in vowels:
    vowel_count += 1
print("Количество гласных:", vowel_count)
Final_sentence = Final_sentence.replace("ugly", "beauty")
print("Предложение без ugly", Final_sentence)

if sentence.startswith("The "):
  print("Начинается с 'The'")
else:
  print("Не начинается с 'The'")

if sentence.endswith(" end"):
  print("Заканчивается на 'end'")
else:
  print("Не заканчивается на 'end'")
