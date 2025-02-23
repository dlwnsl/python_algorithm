N = int(input())
cnt = 0

for i in range(N):
    S = input()
    if list(S) == sorted(S, key = S.find): # 그룹단어가 아니면 새롭게 정렬되므로 false가 됨
        cnt += 1

print(cnt)