import sys

def vsp_check(str):
    stack = []
    result = ''
    for parenthesis in str:
        if parenthesis=='(':
            stack.append(parenthesis)
            result = 'NO'
        if parenthesis==')':          
            if len(stack)>0:
                stack.pop()
                if len(stack)==0:
                    result = 'YES'
                else:
                    result = 'NO'
            else:
                result='NO'

    return result

t = int(sys.stdin.readline())
for _ in range(t):
    ps = sys.stdin.readline()
    print(vsp_check(ps))
