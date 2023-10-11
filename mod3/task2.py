numbers = input()
print([f'двоичная: {bin(int(numbers))}',
       f'Восьмеричная: {oct(int(numbers))}',
       f'Шестнадцатеричная: {hex(int(numbers))}'] if numbers.isdigit() else 'Неверный ввод')

