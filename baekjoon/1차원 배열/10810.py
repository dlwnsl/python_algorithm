N, M = map(int, input().split())
bas=[0]*(N+1)

for _ in range(M):
    i,j,k = map(int, input().split())
    for index in range(i, j+1):
        bas[index]=k

print(*bas[1:])