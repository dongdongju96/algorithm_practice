from re import S


str = input()
result = ''

for s in str:
    if s >= 'a' and s <= 'Z':
        result += chr(ord(s) + 13)
    else:
        result += s

print(result)