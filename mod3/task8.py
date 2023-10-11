phone_number = input("Введите номер телефона: ")
cleaned_phone_number = ''.join(filter(str.isdigit, phone_number))
print(cleaned_phone_number)

