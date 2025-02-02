a = set() # 나머지 집합

for _ in range(10):
    num = int(input())
    a.add(num % 42)

print(len(a)) #len() -> 리스트, 문자열, 튜플, 딕셔너리, 집합 등의 자료형의 길이를 반환하는 함수