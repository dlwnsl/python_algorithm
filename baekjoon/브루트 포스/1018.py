N, M = map(int, input().split())

board = []
count = []

for i in range(N):
    board.append(input())

for a in range(N - 7):
    for b in range(M - 7): # 8 * 8로 자르기 위해 -7
        w_index = 0 # 흰색으로 시작
        b_index = 0 # 검은색으로 시작
        for i in range(a, a + 8): # 시작지점
            for j in range(b, b + 8): # 시작지점
                if (i + j) % 2 == 0: # 짝수인 경우
                    if board[i][j] != 'W': # B라면
                        w_index += 1 # W로 칠하는 개수
                    else:
                        b_index += 1 # B로 칠하는 개수
                else: # 홀수인 경우
                    if board[i][j] != 'W':
                        b_index += 1
                    else:
                        w_index += 1
        
        count.append(w_index) # W로 시작할 때 경우의 수
        count.append(b_index) # B로 시작할 때 경우의 수

print(min(count))