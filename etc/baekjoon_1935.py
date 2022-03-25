n = int(input())
input_str = input()
number_list = []
stack = []

for number in range(n):
    number_list.append(int(input()))

for i in input_str:
    if i >= 'A' and i <= 'Z':
        stack.append(number_list[ord(i)-ord('A')])

    else:
        number_2 = stack.pop()
        number_1 = stack.pop()
        
        
        if i=='+':
            stack.append(number_1 + number_2)
        elif i=='-':
            stack.append(number_1 - number_2)
        elif i=='*':
            stack.append(number_1 * number_2)
        elif i=='/':
            stack.append(number_1 / number_2)
    
print('%.2f' %stack[-1])