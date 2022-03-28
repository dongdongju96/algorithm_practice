input_text = input()
stack = []
result = ''

for i in input_text:
    if i.isalpha():
        result += i # 피연산자면 결과로 추가
    
    else: # 연산자면

        if i=='(':
            stack.append(i) # '(' 가 시작되면 stack에 추가

        elif i=='+' or i=='-':

            while stack and stack[-1]!='(': # 우선순위가 아니면 스택에 있는걸 먼저 결과에 추가
                result += stack.pop()

            stack.append(i) # 스택이 비어있으면 연산자 스택에 추가

        elif i=='*' or i=='/':

            while stack and (stack[-1]=='*' or stack[-1]=='/'): # 우선순위 연산자가 스택에 있으면 먼저 추가
                result += stack.pop()

            stack.append(i)
        
        elif i==')':
            while stack and stack[-1]!='(':
                result += stack.pop()
            stack.pop() # 괄호안 우선순위 연산자 추가

while stack:
    result += stack.pop()

print(result)

"""
stack에 쌓을 때 연산자에 따른 우선순위를 정해서 쌓는다.

×/÷ 와 같은 연산자는 더 높은 우선순위가 없기에 먼저 들어온 ×/÷를 먼저 결괏값에 배치한다
+/- 와 같은 연산자는 가장 우선순위가 낮기에 괄호가 아닌 이상 전부 결괏값에 배치한다.
) 는 ( 가 나오기 전까지의 모든 연산자를 결괏값에 배치한다.
"""