N = int(input())
score = list(map(int, input().split()))

max = max(score)

new_score = [(num / max) * 100 for num in score]
avg = sum(new_score) / N

print(avg)