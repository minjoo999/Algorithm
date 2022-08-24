N = int(input())
score = list(map(int, input().split(' ')))
scores = []
for s in score:
    scores.append(s / max(score)*100)
print(sum(scores) / N)