from itertools import permutations
from collections import deque

def bfs(scv):
    deq = deque([(tuple(scv), 0)])  # 첫 상태와 공격 횟수
    visited = set()  # 방문한 상태를 저장
    
    while deq:
        scv, count = deq.popleft()
        scv = list(scv)
        
        if all(x == 0 for x in scv):
            return count
        
        if tuple(scv) in visited:
            continue
        visited.add(tuple(scv))
        
        for permutate in permutations((9, 3, 1), len(scv)):
            next_scv = [max(0, scv[k] - v) for k, v in enumerate(permutate)]
            deq.append((tuple(next_scv), count + 1))

N = int(input())
scv = list(map(int, input().split()))
print(bfs(scv))