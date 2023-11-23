import re


def check_color_code(color):
    rgb_pattern = r'^rgb\((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\s*,\s*(\d{1,2}|1\d{2}|' \
                  r'2[0-4]\d|25[0-5])\s*,\s*(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\)$'
    hex_pattern = r'^#([a-fA-F0-9]{3}){1,2}$'
    hsl_pattern = r'^hsl\((\d{1,2}|[1-2]\d{2}|3[0-5]\d|360)\s*,\s*(100%|\d{1,2}%)\s*,\s*(100%|\d{1,2}%)\)$'

    if re.match(rgb_pattern, color):
        return True
    elif re.match(hex_pattern, color):
        return True
    elif re.match(hsl_pattern, color):
        return True
    else:
        return False


colors_to_check = [
    "#21f48D",
    "#888",
    "rgb(255, 255, 255)",
    "rgb(10%, 20%, 0%)",
    "hsl(200,100%,50%)",
    "hsl(0, 0%, 0%)",
    "#2345",
    "ffffff",
    "rgb(257, 50, 10)",
    "hsl(20, 10, 0.5)",
    "hsl(34%, 20%, 50%)"
]

for color in colors_to_check:
    if check_color_code(color):
        print(f"{color} - корректный цвет")
    else:
        print(f"{color} - некорректный цвет")