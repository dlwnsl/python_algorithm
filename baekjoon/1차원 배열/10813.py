N, M = map(int, input().split())
bas=list(range(1, N+1))

for _ in range(M):
    i,j=map(int, input().split())
    bas[i-1],bas[j-1]=bas[j-1],bas[i-1]

print(*bas)
