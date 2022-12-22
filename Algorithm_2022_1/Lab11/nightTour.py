def make_graph(n, m):
    # 갈 수 있는 8가지 방향 index로 -> 현재 위치에서 추가해주면 된다
    imove = [-2, -1, 1, 2, 2, 1, -1, -2]
    jmove = [1, 2, 2, 1, -1, -2, -2, -1]
    graph = {i:[] for i in range(n * m)} #딕셔너리 이용해서 i번째 노드가 갈 수 있는 경로를 저장 인접리스트 형태
    for i in range(n):
        for j in range(m):
            for k in range(8): # 8개의 방향
                ni, nj = i + imove[k],j + jmove[k] # 각 좌표별로 들어 갈 수 있는 경로
                if 0 <= ni < n and 0 <= nj < m: # 이동 제한 조건 - 그래프 내부여야 한다.
                    graph[i*m + j].append(ni*m + nj) # 현재위치, 다음위치 
    return graph

# k번째 ( n * m이면 다 찾은 것), v - 현재노드, s-start, n-가로, m-세로, graph-그래프, mark-방문 시 k번째 순서 저장
def tourCycle(k, v, s, n, m, graph, mark):
    global count
    if k == n*m and s in graph[v]: # k == n * m -> 종료 번지까지 도착, graph[v]가 s 즉 현재노드와 s가 같으면 회로 (회로 체크) -> 빼면 경로 문제
        mark[v] = k
        count += 1 # 출력시 방문 경로 알 수 있음
        print("해밀턴 회로 : " + str(mark[0:]))
    else:
        for u in graph[v]: # 현재 노드와 인접 노드 
            if mark[u] == 0: # 방문하지 않은 정점 -> prunning
                mark[u] = k + 1 # k + 1에 u노드 방문하겠다
                tourCycle(k + 1, u, s, n, m, graph, mark) 
                mark[u] = 0 # 재귀 종료 시 u를 0 으로 -> 그래야 모든 정점 방문 가능

                
def tourCircuit(k, v, s, n, m, graph, mark):
    global count
    if k == n * m: # k == n * m이면 회로인지, graph[v]가 s 즉 현재노드와 s가 같으면 회로 (회로 체크) -> 빼면 경로 문제
        mark[v] = k
        count += 1 # 출력시 방문 경로 알 수 있음
        print("해밀턴 경로 : " + str(mark[0:]))
    else:
        for u in graph[v]: # 현재 노드와 인접 노드 
            if mark[u] == 0: # 방문하지 않은 정점 -> prunning
                mark[u] = k + 1 # k + 1에 u노드 방문하겠다
                tourCircuit(k + 1, u, s, n, m, graph, mark) 
                mark[u] = 0 # 재귀 종료 시 u를 0 으로 -> 그래야 모든 정점 방문 가능


# input
n, m = map(int, input().split()) # 행 크기 열 크기
T = int(input()) # 출발점 개수

graph = make_graph(n, m) # 그래프 만들기 

mark = [0] * (n * m)
count = 0

starts = []
for _ in range(T):
    starts.append(list(map(int, input().split())))

# output
# 해밀턴 회로
mark[0] = 1 # 출발 노드 0가 순서 첫번째
tourCycle(1, 0, 0, n, m, graph, mark)
print("해밀턴 회로 횟수 : " + str(count))

# 해밀턴 경로
for start in starts:
    count = 0
    # 초기화
    for i in range(len(mark)):
        mark[i] = 0

    mark[start[0]* m + start[1]] = 1 # 출발 노드 방문 처리 -> 출발노드가 1번째
    tourCircuit(1, start[0]* m + start[1], start[0]* m + start[1], n, m, graph, mark)
    print("해밀턴 경로 횟수 : " + str(count))
    
