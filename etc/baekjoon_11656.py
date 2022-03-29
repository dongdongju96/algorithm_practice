input_str = input()
stack = []

for i in range(len(input_str)):
    stack.append(input_str[i:])

for i in sorted(stack):
    print(i)