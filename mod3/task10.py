size = int(input("Введите размерность квадратной матрицы: "))

# Генерируем и выводим исходную матрицу
for i in range(1, size + 1):
    row = ', '.join(str(x) for x in range(1, size + 1))
    print(row)

# Создаем транспонированную матрицу и выводим ее
print("         ")
for i in range(1, size + 1):
    row = ', '.join(str(i) for _ in range(1, size + 1))
    print(row)

4