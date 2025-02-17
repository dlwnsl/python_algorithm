N = int(input())

cnt = 0
num = 666

while True:
    s_num = str(num)
    if '666' in s_num:
        cnt += 1

    if N == cnt:
        break
    num += 1

print(num)