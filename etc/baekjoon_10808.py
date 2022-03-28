str = input()

li = [0] * 26

for i in str:
    li[ord(i)-ord('a')] += 1

print(*li)

