N = int(input())

if N == 1:
    print('')

for i in range(2, N+1):
    if N % i == 0:
        while N % i == 0:
            print(i)
            N = N / i

# 다른 풀이
N = int(input())

n = 2

while N > 1:
    if N % n == 0:
        print(n)
        N = N // n
    else:
        n += 1
        if n > int(N**0.5):
            n = N