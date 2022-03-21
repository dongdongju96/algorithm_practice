n = int(input())
nge = list(map(int,input().split()))

for i in range(n):

    if i==n-1:
        print(-1)
        break
    else:
        standard = nge[i]
        stack = []
        for j in nge[i+1:]:
            if standard < j:
                stack.append(j)

        if stack:
            print(stack[0], end=' ')
        else:
            print(-1, end=' ')