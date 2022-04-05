str = input().rstrip('\n')
print(str)
stack = [0]*4

for s in str:
    if ord(s)>=ord('a') and ord(s)<=ord('z'):
        stack[0] = stack[0] + 1
    elif ord(s)>=ord('A') and ord(s)<=ord('Z'):
        stack[1] = stack[1] + 1
    elif ord(s)>=ord('0') and ord(s)<=ord('9'):
        stack[2] = stack[2] + 1
    elif ord(s)==ord(' '):
        stack[3] = stack[3] + 1
print(*stack)