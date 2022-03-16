n, k = map(int,input().split())


table_list = [i for i in range(1,n+1)]
result_list = []
index = 0

while len(table_list) > 0:
    if len(table_list) < k:
        for _ in range(k):
            index += 1
            if index>=len(table_list)-1:
                index = 0
            
    elif index + k > len(table_list):
        new_index = len(table_list) - (index + k - 1)
        if new_index < 0:
            index = -new_index
        else:
            index = new_index
    else:
        index = index + k - 1
    result_list.append(table_list[index])
    table_list.pop(index)

print('<',end='')
for i in result_list:
    print(f'{i}, ',end='')
print('>',end='')