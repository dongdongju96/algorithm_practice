n = int(input())
input_str = input()
number_list = []
stack = []

for number in range(n):
    number_list.append(int(input()))

for i in input_str:
    if i=='+':
        number_1 = stack.pop()
        number_2 = stack.pop()
        stack.append(number_1 + number_2)
    
    elif i=='-':
        number_1 = stack.pop()
        number_2 = stack.pop()
        stack.append(number_1 - number_2)
        
    elif i=='*':
        number_1 = stack.pop()
        number_2 = stack.pop()
        stack.append(number_1 * number_2)

    elif i=='/':
        number_1 = stack.pop()
        number_2 = stack.pop()
        stack.append(number_1 / number_2)

    else:
        stack.append(number_list[ord(i)-ord('A')])
    
print(stack[-1])