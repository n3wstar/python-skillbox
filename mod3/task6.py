words = input("Введите список слов: ").split()
new_word = ''.join([word[-1] for word in words])
print(new_word)

