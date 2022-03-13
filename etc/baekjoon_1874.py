# 시간 초과 풀이
#  import sys

# n = int(sys.stdin.readline())
# result_list = []
# print_list = []
# temp_list = []
# idx = 0
# count = 1
# result = ''

# for i in range(1,n+1):
#     number = int(sys.stdin.readline())
#     result_list.append(number)

# while idx<n:
#     if result_list[idx] in temp_list:
#         if temp_list[-1]==result_list[idx]:
#             idx += 1
#             del temp_list[-1]
#             print_list.append('-')
#         else:
#             result = 'NO'
#             break
#     else:
#         temp_list.append(count)
#         count += 1
#         print_list.append('+')

# if result=='NO':
#     print(result)
# else:    
#     for syb in print_list:
#         print(syb)


import sys

n = int(sys.stdin.readline())
result_list = []
print_list = []
count = 1
result = ''

for i in range(1,n+1):
    number = int(sys.stdin.readline())
    while count <= number:
        result_list.append(count)
        print_list.append('+')
        count += 1

    if result_list[-1] == number:
        result_list.pop()
        print_list.append('-')
    else:
        result='NO'

if result=='NO':
    print(result)
else:
    for i in print_list:
        print(i)