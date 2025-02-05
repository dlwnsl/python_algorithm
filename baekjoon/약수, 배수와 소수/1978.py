N = int(input())
X = list(map(int, input().split()))

total = 0

for i in X:
    cnt = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
        
        if cnt == 0:
            total += 1

print(total)
