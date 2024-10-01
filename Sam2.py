import random

def main():
  roll = random.randint(1, 6)
  print(f"Результат: {roll}")

  if roll in (5, 6):
    print("Вы победили")
  elif roll in (3, 4):
    print("Анлаки...")
    main()
  else:
    print("Вы проиграли")

if __name__ == "__main__":
  main()
