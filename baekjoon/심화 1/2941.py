arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
S = input()

for i in arr:
    S = S.replace(i, "*")

print(len(S))

