from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(1, N):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
visited = [False] * (N + 1)
distance = [0] * (N + 1)

total = 0
deq = deque([1])
visited[1] = True
while deq:
    count = 0
    node = deq.popleft()
    for i in graph[node]:
        if visited[i] == False:
            deq.append(i)
            visited[i] = True
            distance[i] = distance[node] + 1

for i in range(2, N + 1):
    if len(graph[i]) == 1:
        total += distance[i]

if total % 2 != 0:
    print("Yes") 
else: print("No")



