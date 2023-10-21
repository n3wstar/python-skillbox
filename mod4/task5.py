def count_letter_frequency(file_path):
    letter_frequency = {}

    try:
        with open(file_path, 'r') as file:
            text = file.read()

            for char in text:
                if char.isalpha():
                    char = char.lower()
                    if char in letter_frequency:
                        letter_frequency[char] += 1
                    else:
                        letter_frequency[char] = 1

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return

    sorted_frequency = sorted(letter_frequency.items(), key=lambda x: x[1])

    with open("counter.txt", "w") as output_file:
        for char, count in sorted_frequency:
            output_file.write(f"{char}: {count}\n")

    print("Результат записан в counter.txt")


file_path = input("Введите путь к файлу: ")
count_letter_frequency(file_path)
