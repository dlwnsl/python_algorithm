N = int(input())

paper = [[0]*100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

total = 0

for row in paper:
    total += row.count(1)

print(total)