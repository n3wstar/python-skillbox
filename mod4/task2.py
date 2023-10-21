def exponentiation(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return exponentiation(a * a, n // 2)
    else:
        return a * exponentiation(a, n - 1)


a = int(input("Введите число: "))
n = int(input("Введите степень: "))

result = exponentiation(a, n)
print(f"{a} в степени {n} равно {result}")
