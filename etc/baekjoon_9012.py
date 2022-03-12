import sys

def vsp_check(str):
    stack = []
    result = 'NO'
    for parenthesis in str:
        if parenthesis=='(':
            stack.append(parenthesis)
        else:
            if len(stack)>0:
                stack.pop()
                if len(stack)>0:
                    result = 'NO'
                else:
                    result = 'YES'
            else:
                result='NO'
    return result

t = int(sys.stdin.readline())
for _ in range(t):
    ps = sys.stdin.readline()
    print(vsp_check(ps))
