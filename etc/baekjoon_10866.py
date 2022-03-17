import sys

n = int(sys.stdin.readline())

deque = []

for _ in range(n):
    command_list = sys.stdin.readline().split()
    print(command_list)
    print(deque)
    if command_list[0]=='push_front':
        deque = [command_list[1]] + deque
    
    elif command_list[0]=='push_back':
        deque.append(command_list[1])
    
    elif command_list[0]=='pop_front':
        if len(deque)!=0:
            print(deque[0])
            del deque[0]
        else:
            print(-1)

    elif command_list[0]=='pop_back':
        if len(deque)!=0:
            print(deque[-1])
            del deque[-1]
        else:
            print(-1)
            
    elif command_list[0]=='size':
        print(len(deque))

    elif command_list[0]=='empty':
        if len(deque)!=0:
            print(0)
        else:
            print(1)

    elif command_list[0]=='front':
        if len(deque)!=0:
            print(deque[0])
        else:
            print(-1)
    
    elif command_list[0]=='back':
        if len(deque)!=0:
            print(deque[-1])
        else:
            print(-1)