x = y = 0

for _ in range(3):
    a, b = map(int, input().split())
    x ^= a
    y ^= b

print(x, y)

# XOR(Exclusive OR) 연산은 두 비트가 서로 다를 때 1을 반환하고, 같을때는 0을 반환
# XOR 연산은 기호로 '^'로 나타내며, 예를 들어, A XOR B는 A와 B가 다를 때 1, 같을 때 0을 반환
# ex) 0 ^ A = A, XOR 연산은 교환 법칙과 결합 법칙이 성립함


