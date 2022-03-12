import sys

# def vsp_check(str):
#     stack = []
#     result = ''
#     for parenthesis in str:
#         if parenthesis=='(':
#             stack.append(parenthesis)
#             result = 'NO'
#         if parenthesis==')':          
#             if len(stack)>0:
#                 stack.pop()
#                 if len(stack)==0:
#                     result = 'YES'
#                 else:
#                     result = 'NO'
#             else:
#                 result='NO'

#     return result

def vsp_check(str):
    sum = 0
    result = ''
    for parenthesis in str:
        if parenthesis=='(':
            sum += 1
        elif parenthesis==')':
            sum += -1
        if sum < 0:    ## 놓친 포인트
            break
        
    if sum==0:
        result = 'YES'
    else:
        result = 'NO'

    return result

t = int(sys.stdin.readline())
for _ in range(t):
    ps = sys.stdin.readline()
    result = vsp_check(ps)
    print(result)


# 반례 )(),(()