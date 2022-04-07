def get_g(a,b):
    if a>=b:
        while a%b>0:
            r = a%b
            a = b
            b = r
    else:
        while a%b>0:
            r = a%b
            a = b
            b = r # b는 최대 공약수
    return b

a, b = map(int,input().split())

g = get_g(a,b)
result = a*b/g

print(g)
print(int(result))