from collections import Counter

# n = int(input())
# input_list = list(map(int,input().split()))
# count = Counter(input_list)
# result_list = [-1]*n
# stack = []
# print(count[1])
# for i in range(n):
#     print(stack)
#     while stack:
#         if count[input_list[i]] > count[input_list[stack[-1]]]:
#             result_list[i] = input_list[stack.pop()]
#         else:
#             break
        
#     if not stack:
#         stack.append(i)

# print(*result_list)

n = int(input())
input_list = list(map(int,input().split()))
count = Counter(input_list)
result_list = [-1]*n
stack = []

for i in range(n):
    
    while stack:
        if count[input_list[i]] > count[input_list[stack[-1]]]:
            result_list[stack.pop()] = input_list[i]
        else:
            break
        
    stack.append(i)

print(*result_list)