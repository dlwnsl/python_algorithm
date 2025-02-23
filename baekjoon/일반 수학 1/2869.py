import math

A, B, V = map(int, input().split())

# 올라가야 할 거리 = V - B

if (V-B) % (A-B) == 0:
    print((V-B)//(A-B))
else:
    print((V-B)//(A-B)+1)

# 다른 풀이

A, B, V = map(int, input().split())

day = (V-B)/(A-B)
print(math.ceil(day))

# ceil 함수는 실수를 올림하여 정수를 반환하는 함수