def process_word(word):
    return word.lower().replace(" ", "")


def is_palindrome(word):
    processed_word = process_word(word)
    return processed_word == processed_word[::-1]


def create_palindrome(word):
    processed_word = process_word(word)
    if is_palindrome(processed_word):
        return processed_word
    else:
        for i in range(len(word)):
            remaining_chars = word[:i] + word[i + 1:]
            if is_palindrome(remaining_chars):
                return remaining_chars
    return None


input_word = input("Введите слово: ")
palindrome = create_palindrome(input_word)
if palindrome:
    print("Можно составить палиндром:", palindrome)
else:
    print("Из данного слова нельзя составить палиндром.")