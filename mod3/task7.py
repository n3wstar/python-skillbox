numbers = input("Введите последовательность чисел, разделенных пробелами: ").split()
result = len(numbers) != len(set(map(int, numbers)))
print(result)

