s = input()
if s.isnumeric():
    if len(set(s)) < len(s):
        print(True)
    else:
        print(False)

