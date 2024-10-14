user_input = input("Введите последовательность чисел, разделенных пробелом: ")

number_strings = user_input.split()
numbers = [int(num) for num in number_strings]

numbers_tuple = tuple(numbers)

print("Список:", numbers)
print("Кортеж:", numbers_tuple)