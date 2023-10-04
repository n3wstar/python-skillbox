def count_beginning_symbol(s, i):
    count = 0
    for char in s:
        if char == i:
            count += 1
        else:
            break
    return count


s, i = input("Введите строку и символ через запятую: ").split(',')


result = count_beginning_symbol(s, i)
print(result)