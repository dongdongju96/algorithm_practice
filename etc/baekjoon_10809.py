s = input()
li = [-1] * 26
stack = []

for index, alphabet in enumerate(s):
    if alphabet not in stack:
        stack.append(alphabet)
        li[ord(alphabet)-ord('a')] = index
    
print(*li)