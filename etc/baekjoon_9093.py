import sys

t = int(sys.stdin.readline())

for _ in range(t):
    sentence_list = sys.stdin.readline().split()
    for word in sentence_list:
        print(word[::-1],end=' ')
