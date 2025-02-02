S = list(input())
W = list(reversed(S))

if S == W:
    print(1)
else:
    print(0)

# 다른 풀이
word = list(input())
if word == word[::-1] :
    print(1)
else :
    print(0)
