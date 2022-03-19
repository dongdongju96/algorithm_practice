import sys
from collections import deque

dec = deque()
stack = []
result = ''
state = True # 단어를 뒤집을 때 True

str = input()

for spell in str:
    if spell=='<':
        dec.append(spell)
        while stack:
            result += stack.pop()
        state = False
    
    elif spell=='>':
        dec.append(spell)
        while dec:
            result += dec.popleft()
        state = True
        

    elif spell==' ':
        while stack:
            result += stack.pop()
        while dec:
            result += dec.popleft()
        result += ' '
        
    else:
        if state:
            stack.append(spell)
        else:
            dec.append(spell)

while stack:
    result += stack.pop()
    
print(result)