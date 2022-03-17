import sys

n = int(input())

deque = []

for _ in range(n):
    command_list = sys.stdin.readline().split()
    if command_list[0]=='push_front':
        deque = list(command_list[1]) + deque
    
    elif command_list[0]=='push_back':
        deque.append(command_list[1])
    
    elif command_list[0]=='pop_front':
        if deque:
            print(deque[0])
            del deque[0]
        else:
            print(-1)

    elif command_list[0]=='pop_back':
        if deque:
            print(deque[-1])
            del deque[-1]
        else:
            print(-1)
            
    elif command_list[0]=='size':
        print(len(deque))

    elif command_list[0]=='empty':
        if deque:
            print(0)
        else:
            print(1)

    elif command_list[0]=='front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    
    elif command_list[0]=='back':
        if deque:
            print(deque[-1])
        else:
            print(-1)