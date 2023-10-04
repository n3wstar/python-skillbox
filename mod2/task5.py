i = input()
n = int(input())

alphabet = 'abcdefghijklmnopqrstuvwxyz'

index_i = alphabet.index(i)

index_k = (index_i + n)

k = alphabet[index_k]

print(k)

