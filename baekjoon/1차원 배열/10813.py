N, M = map(int, input().split())
bas=list(range(1, N+1))

for _ in range(M):
    i,j=map(int, input().split())
    bas[i-1],bas[j-1]=bas[j-1],bas[i-1]

print(*bas)

print(bas)   # 리스트 자체 출력
print(*bas)  # 리스트 요소를 공백으로 구분하여 출력