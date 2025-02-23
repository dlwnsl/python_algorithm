G_dic = { "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0 }

total_N = 0 # 학점 총합
total_NG = 0 # 학점 x 평점 총합

for _ in range(20):
    S, N, G = input().split()
    N = float(N)

    if G != "P":
        total_NG += N * G_dic[G]
        total_N += N

if total_N != 0:
    a = total_NG / total_N
else:
    a = 0.0

print(format(a, "6f"))