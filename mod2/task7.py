
input_string = input("Введите строку из 0 и 1: ")


def equality_check(string):
    count_zeros = string.count('0')
    count_ones = string.count('1')
    if count_zeros == count_ones:
        return 'yes'
    else:
        return 'no'


result = equality_check(input_string)
print(result)
