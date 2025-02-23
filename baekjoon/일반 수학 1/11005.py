N, B = map(int, input().split())

# B진법 변환 -> 더 안나눠질 때까지 B로 계속 나눈 뒤 나머지를 저장


arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ex) 나머지가 10이면 arr[10] = 'A'

result = ''

if N == 0:
    result = '0'
else:
    while N > 0:
        R = N % B
        result = arr[R] + result 
        N //= B 

print(result) 
