a = int(input())
b = int(input())
c = int(input())

if a==b==c==60:
    print('Equilateral')
elif (a==b and a + b + c == 180) or (a==c and a + b + c == 180) or (b==c and a + b + c == 180):
    print('Isosceles')
elif a!=b!=c and a + b + c == 180:
    print('Scalene')
else:
    print('Error')

# 다른 풀이
a = int(input())
b = int(input())
c = int(input())
if a+b+c == 180:
    if a == b == c == 60:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
