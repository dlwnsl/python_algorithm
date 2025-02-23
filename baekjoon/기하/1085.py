x, y, w, h = map(int, input().split())

a = x
b = w - x
c = y
d = h - y

print(min(a, b, c, d))