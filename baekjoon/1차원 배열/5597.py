stu=set(range(1,31)) # 전체 학생

sub={int(input()) for _ in range(28)} # 제출한 학생 입력받기 {}집합으로 저장, 집합을 사용하면 중복이 자동으로 제거됨

none=sorted(stu - sub) # 차집합, sorted 사용하여 작은 번호부터 정렬

print(none[0])
print(none[1])