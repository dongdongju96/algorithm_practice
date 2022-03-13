import sys

def L(input_list):
    cursor_location = input_list.index('cursor')
    if cursor_location!=0:
        input_list.remove('cursor')
        input_list.insert(cursor_location-1,'cursor')
    else:
        pass
    

def D(input_list):
    cursor_location = input_list.index('cursor')
    if cursor_location!=len(input_list)-1:
        input_list.remove('cursor')
        input_list.insert(cursor_location+1,'cursor')
    else:
        pass

def B(input_list):
    cursor_location = input_list.index('cursor')
    if cursor_location!=0:
        del input_list[cursor_location-1]
    else:
        pass

def P(input_list, text):
    cursor_location = input_list.index('cursor')
    input_list.insert(cursor_location-1, text)

input_text = sys.stdin.readline()
input_text = list(input_text)
input_text.pop()
input_text.append('cursor')
m = int(sys.stdin.readline())
for _ in range(m):
    command = sys.stdin.readline()
    command_list = command.split()
    if command_list[0]=='P':
        P(input_text, command_list[1])
    elif command_list[0]=='L':
        L(input_text)
    elif command_list[0]=='D':
        D(input_text)
    else:
        B(input_text)
input_text.remove('cursor')
print(''.join(input_text))