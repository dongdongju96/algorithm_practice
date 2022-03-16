n, k = map(int,input().split())


table_list = [i for i in range(1,n+1)]
result_list = []
index = 0

while len(table_list) > 0:
    index = index + k - 1
    if index >= len(table_list)-1:
        index = index%len(table_list)
    result_list.append(table_list[index])
    table_list.pop(index)

print('<',end='')
print(', '.join(map(str,result_list)),end='')
print('>')