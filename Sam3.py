def analyze_text(directory):
    with open(directory, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    total_letters = 0
    total_words = 0
    total_lines = len(lines)
    for line in lines:
        total_letters += sum(c.isalpha() and c.isascii() for c in line)
        total_words += len(line.split())
    print(f"Количество букв латинского алфавита: {total_letters}")
    print(f"Количество слов: {total_words}")
    print(f"Количество строк: {total_lines}")

analyze_text(r'C:\Users\Глеб\PycharmProjects\lab_1\input.txt')
