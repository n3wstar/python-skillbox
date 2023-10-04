
decimal_number = int(input("Введите натуральное число в десятичной системе: "))
if decimal_number < 1:
        print("Неверный ввод: Введите натуральное число больше 0")
else:
    binary_representation = bin(decimal_number).replace("0b", "")
    octal_representation = oct(decimal_number).replace("0o", "")
    hexadecimal_representation = hex(decimal_number).replace("0x", "")
    print(f"Двоичное представление: {binary_representation}")
    print(f"Восьмеричное представление: {octal_representation}")
    print(f"Шестнадцатеричное представление: {hexadecimal_representation}")



