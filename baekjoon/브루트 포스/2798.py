N, M = map(int, input().split())
arr = list(map(int, input().split()))

max = 0

for i in range(N):
    for j in range(i+1, N):
        for z in range(j+1, N):
            res = arr[i] + arr[j] + arr[z]
            if res == M:
                print(res)
                exit()
            if res < M and M - res < M - max:
                max = res
print(max)
    