import sys
input = sys.stdin.readline

n = int(input())
input_list = list(map(int,input().split()))

stack = []
result = [-1] * n

for i in range(n):
    while stack:
        if input_list[i] > input_list[stack[-1]]:
            result[stack.pop()] = input_list[i]            
        else:
            break
    stack.append(i)

print(*result)