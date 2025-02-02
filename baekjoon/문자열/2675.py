T = int(input().strip())

for _ in range(T):
    R, S = input().split()
    R = int(R)

    P = "".join([i * R for i in S])

    print(P)