import re


def check_password(passw):
    if len(passw) < 6:
        return False

    if len(re.findall(r'[A-Z]', passw)) < 2:
        return False

    if not re.search(r'\d', passw):
        return False

    if len(set(re.findall(r'[!@#$%^&*?]', passw))) < 2:
        return False

    if re.search(r'(.)\1\1', passw):
        return False

    if not re.fullmatch(r'[A-Za-z0-9!@#$%^&*?]+', passw):
        return False

    return True


passwords_to_check = [
    'rtG3FG!Tr^e',
    'aA1!*!1Aa',
    'oF^a1D@y5e6',
    'enroi#$rkdeR#$092uWedchf34tguv394h',
    'пароль',
    'password',
    'qwerty',
    'lOngPa$$$W0Rd'
]

for password in passwords_to_check:
    if check_password(password):
        print(f'Пароль "{password}" корректный')
    else:
        print(f'Пароль "{password}" некорректный')
