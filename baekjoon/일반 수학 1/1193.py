# 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> 1/3 -> 1/4 -> 2/3 -> 3/2 -> 4/1 ...
X = int(input())

line = 0 
end = 0 # 맨 끝의 숫자 번호

while X > end:
    line += 1
    end += line

K = end - X

if line % 2 == 0: # 짝수 라인일 때
    a = line - K # 분자
    b = K + 1 # 분모
else:
    a = K + 1
    b = line - K

print(str(a) + '/' + str(b))

# 다른 풀이

n = int(input())
line = 1

while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    up = n
    down = line - n + 1
else:
    up = line - n + 1
    down = n

print(up,'/',down, sep="")