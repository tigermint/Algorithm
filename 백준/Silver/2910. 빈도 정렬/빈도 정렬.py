from collections import Counter

N, C = list(map(int, input().split()))
sequences = list(map(int, input().split()))
c = Counter(sequences)
for key, value in c.most_common():
    for _ in range(value):
        print(key, end=" ")
print()
