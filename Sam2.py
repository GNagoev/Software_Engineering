def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read()
            if not data:
                raise Exception("В этом файле ничего нет")
            else:
                print(data)
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    empty_file = "empty_file.txt"
    non_empty_file = "non_empty_file.txt"

    print("Считывание пустого файла:")
    read_file(empty_file)

    print("\nСчитывание не пустого файла:")
    read_file(non_empty_file)
