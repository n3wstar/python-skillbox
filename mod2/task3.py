a = int(input())
b = int(input())
c = int(input())

min_number = min(a, b, c)
max_number = max(a, b, c)
middle_number = a + b + c - min_number - max_number
print(middle_number)

