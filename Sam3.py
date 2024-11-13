def add_two_numbers():
    try:
        num = input("Введите число: ")
        result = 2 + int(num)
        print(f"2 + ваше число = {result}")
    except ValueError:
        print("Неподходящий тип данных.Ожидалось целое число!")


if __name__ == '__main__':
    add_two_numbers()
    add_two_numbers()
    add_two_numbers()
    add_two_numbers()
    add_two_numbers()
    add_two_numbers()
    add_two_numbers()
