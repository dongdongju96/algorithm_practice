s = input()
li = [-1] * 28
index = 0

for alphabet in s:
    li[ord(alphabet)-ord('a')] = index
    index += 1

print(*li)