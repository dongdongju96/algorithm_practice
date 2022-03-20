input_text = input()

stack = []
result = 0 # 잘려진 쇠막대기 조각 총 개수


for i in range(len(input_text)):
    if input_text[i]=='(':
        stack.append('(')

    # input_text[i] 가 ')' 인 경우
    else:
        if input_text[i-1]=='(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)