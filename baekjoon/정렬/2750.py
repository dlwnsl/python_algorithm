N = int(input())
arr = []

for i in range(N):
    num = int(input())
    arr.append(num)

for i in sorted(arr):
    print(i)