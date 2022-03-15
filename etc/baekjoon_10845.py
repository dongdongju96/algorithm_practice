import sys # 추가
n = int(input())

que = []

for _ in range(n):
    command_list = list(sys.stdin.readline().split()) # 변경
    
    if command_list[0]=='push':
        que.append(command_list[1])

    elif command_list[0]=='pop':
        if len(que)!=0:
            print(que[0])
            del que[0]
        else:
            print(-1)
        
    elif command_list[0]=='size':
        print(len(que))
        
    elif command_list[0]=='empty':
        if len(que)==0:
            print(1)
        else:
            print(0)
        
    elif command_list[0]=='front':
        if len(que)!=0:
            print(que[0])
        else:
            print(-1)

    elif command_list[0]=='back':
        if len(que)!=0:
            print(que[-1])
        else:
            print(-1)
    else:
        raise
