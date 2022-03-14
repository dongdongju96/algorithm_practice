import sys

# def L(cursor):
#     if cursor > 1:
#         cursor = cursor - 1        
#     else:
#         return cursor

#     return cursor

# def D(cursor,input_text):
#     if cursor < len(input_text)+1:
#         cursor = cursor + 1
#     else:
#         return cursor

#     return cursor

# def B(cursor,input_text):
#     if cursor > 1:
#         del input_text[cursor-2]
#         cursor = cursor - 1
#     else:
#         return cursor, input_text

#     return cursor, input_text

# def P(cursor, input_text, text):
#     input_text.insert(cursor-1, text)
#     cursor = cursor + 1

#     return cursor, input_text


input_text = list(input())
temp_list = [] # 임시 리스트

m = int(input())

for _ in range(m):
    command = sys.stdin.readline()
    command_list = command.split()
    if command_list[0]=='L':
        if len(input_text)>=1:
            temp_list.append(input_text[-1])
            input_text.pop()
        else:
            pass
    elif command_list[0]=='D':
        if len(temp_list) >= 1:
            input_text.append(temp_list[-1])
            temp_list.pop()
        else:
            pass
    elif command_list[0]=='B':
        if len(input_text)>=1:
            input_text.pop()
        else:
            pass
    else:
        input_text.append(command_list[1])

# 최종 출력
input_text = input_text + temp_list[::-1]
print(''.join(input_text))