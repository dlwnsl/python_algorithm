N, M = map(int, input().split())
bas = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, input().split())
    bas[i-1:j] = bas[i-1:j][::-1] # 리스트 슬라이싱 -> 역순 변환

print(*bas)
