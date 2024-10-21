def read_and_convert(directory):
    with open(directory, 'r', encoding='utf-8') as file:
        content = file.read()
    modified_content = content.lower()
    print(modified_content)

read_and_convert(r'C:\Users\Глеб\PycharmProjects\lab_1\input.txt')
