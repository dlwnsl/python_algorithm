# 234567 까지는 2개 -> 6 2
# 8910111213141516171819 까지는 3개 -> 12 3
# 202122232425262728293031323334353637 까지는 4개 -> 18 4
# ... 

N = int(input())

cnt = 1
ans = 1
while cnt < N:
    cnt += 6*ans
    ans += 1

print(ans)