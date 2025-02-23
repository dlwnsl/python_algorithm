S = input().strip()

al = "abcdefghijklmnopqrstuvwxyz"

index = []

for i in al:
    index.append(str(S.find(i))) 
    # find() 는 해당 문자가 S에서 처음 등장하는 위치를 반환
    # 문자가 존재하지 않으면 -1을 반환

print(" ".join(index)) 
# join()으로 연결하여 출력