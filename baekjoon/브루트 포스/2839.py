N = int(input())

cnt = 0

while N >= 0:
    if N % 5 == 0:
        cnt += (N // 5)
        print(cnt)
        break
    N -= 3 # 음수가 되면 cnt가 N에 정확하게 나누어 떨어지지 않음
    cnt += 1 
else:
    print(-1)