N, X = map(int, input().split())  # 첫 번째 줄 입력: N과 X
A = list(map(int, input().split()))  # 두 번째 줄 입력: 수열 A

result = [str(num) for num in A if num < X]
print(" ".join(result))