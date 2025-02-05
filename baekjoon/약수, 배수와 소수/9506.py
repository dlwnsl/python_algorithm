while True:
    n = int(input())
    if n == -1:
        break
    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    if sum(arr) == n:
        print(n, "=", " + ".join(str(i) for i in arr))
        # print(n, " = ", " + ".join(str(i) for i in arr), sep="") 와 같음
    else:
        print(n, "is NOT perfect.")

# sep="" -> print() 함수에서 여러 개의 인자를 출력할 때, 그 사이에 삽입되는 문자열을 지정하는 옵션