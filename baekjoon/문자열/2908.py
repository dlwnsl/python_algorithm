A, B = input().split()

a = int(A[::-1])
b = int(B[::-1])

print(max(a,b))

# 정수형은 [::-1]로 뒤집을 수 없음