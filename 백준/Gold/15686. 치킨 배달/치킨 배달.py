from itertools import combinations
import sys
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chickens = []; houses = []
for i in range(len(city)):
    for j in range(len(city)):
        if city[i][j] == 1: houses.append([i, j])
        if city[i][j] == 2: chickens.append([i, j])

combis = list(combinations(chickens, M))
min_distance = sys.maxsize

for combi in combis:
    sum_distance = 0
    for house in houses:
        distance = sys.maxsize
        for chicken in combi:
            distance = min(distance, abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
        sum_distance += distance
    min_distance = min(min_distance, sum_distance)
print(min_distance)
        