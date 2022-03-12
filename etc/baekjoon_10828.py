def push(input_list,X):
    input_list.append(X)
    
def pop(input_list):
    if len(input_list)>0:
        pop_val = input_list[-1]
        del input_list[-1]
        print(pop_val)
    else:
        print('-1')

def size(input_list):
    print(len(input_list))

def empty(input_list):
    if len(input_list)==0:
        print('1')
    else:
        print('0')

def top(input_list):
    if len(input_list)>0:
        print(input_list[-1])
    else:
        print(-1)

import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    input_val = sys.stdin.readline().split()
    if input_val[0]=='push':
        push(stack,input_val[1])
    elif input_val[0]=='pop':
        pop(stack)
    elif input_val[0]=='size':
        size(stack)
    elif input_val[0]=='empty':
        empty(stack)
    else:
        top(stack)


# 첫 번째 시도에 에러가 난 이유는 input()을 사용해서 그렇다
# sys.stdin.readline()을 사용하면 된다.