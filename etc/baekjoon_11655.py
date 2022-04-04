input_text = input()
stack = []

for char in input_text:
    if ord(char)>=97 and ord(char)<=122:
        if ord(char)+13 > 122:
            stack.append(chr(13 - (122 - ord(char)) + 96))
        else:
            stack.append(chr(ord(char)+13))
    
    elif ord(char)>=65 and ord(char)<=90:
        if ord(char)+13 > 90:
            stack.append(chr(13 - (90 - ord(char)) + 64))
        else:
            stack.append(chr(ord(char)+13))
    else:
        stack.append(char)

for i in stack:
    print(i,end='')

# 다른 사람의 풀이

# s = input()
# res = ''
# for c in s:
#     if 'a' <= c <= 'z':
#         res += chr((ord(c)+13) if c <= 'm' else ord(c)-13)
#     elif 'A' <= c <= 'Z':
#         res += chr((ord(c)+13) if c <= 'M' else ord(c)-13)
#     else:
#         res += c
# print(res)