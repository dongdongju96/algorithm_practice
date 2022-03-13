import sys

def L(cursor):
    if cursor > 1:
        cursor = cursor - 1        
    else:
        return cursor

    return cursor

def D(cursor,input_text):
    if cursor < len(input_text)+1:
        cursor = cursor + 1
    else:
        return cursor

    return cursor

def B(cursor,input_text):
    if cursor > 1:
        del input_text[cursor-2]
        cursor = cursor - 1
    else:
        return cursor, input_text

    return cursor, input_text

def P(cursor, input_text, text):
    input_text.insert(cursor-1, text)
    cursor = cursor + 1
    
    return cursor, input_text


input_text = sys.stdin.readline()
input_text = list(input_text)
input_text.pop()

# 커서는 맨 뒤에 위치
cursor = len(input_text)+1

m = int(sys.stdin.readline())

for _ in range(m):
    command = sys.stdin.readline()
    command_list = command.split()
    if command_list[0]=='P':
        cursor, input_text = P(cursor,input_text, command_list[1])
    elif command_list[0]=='L':
        cursor = L(cursor)
    elif command_list[0]=='D':
        cursor = D(cursor, input_text)
    else:
        cursor, input_text = B(cursor,input_text)

# 최종 출력
print(''.join(input_text))