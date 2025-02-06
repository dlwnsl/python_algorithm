a, b = map(int, input().split())
C = int(input())
n = int(input())

if (a*n + b) <= C*n and a<=C :
    print(1)
else:
    print(0)