def m_coloring(i):
    global count # 현재 발견한 solution 개수
    global m # 현재 사용 색깔 개수
    # 탐색
    if promising(i):
        if i == n: # 끝까지 탐색 -> 정답
            count+=1
        else:
            for color in range(1, m + 1): # 모든 가능 색깔 탐색
                vcolor[i + 1] = color
                m_coloring(i + 1) # 다음 재귀로 넘어가고 불가능하다면 backTracking
                
 

def promising(i):
    j = 1 #SST를 탐색
    flag = True
    # pruning 전략 : level 1 부터 현재 SST의 level인 i까지 탐색할 경우 연결되어 있는데 색깔이 같은 경우 False
    while j < i and flag:
        # vertex 인접된거 생각할 때 전 노드만 생각하면 안된다 -> 인접한 노드도 생각해야 한다
        if W[i][j] and vcolor[i] == vcolor[j]: #W[i][j]가 연결되어 있으며, 두 노드의 색깔이 같다면
            flag = False
        j += 1
    return flag



#input
n ,k = map(int, input().split()) # n : 노드 개수, k : 인접 노드 list

W = [[0]*(n + 1) for _ in range(n + 1)] # adjacency matrix, undirected

# 인접한 부분은 모두 1로 연결 표시
for _ in range(k):
    a,b = map(int, input().split())
    W[a][b] = 1
    W[b][a] = 1

m = 1 # color 개수
vcolor = [0]*(n + 1) #노드 개수 (0, 1번, 2번, 3번, ... n번)

# 사용 색깔을 2개부터... 모두 다른 색깔로 블럭을 칠할 수 있는 최소의 색깔 구하고, 그 조합도 구한다. 
while True:
    count = 0
    m_coloring(0) #return count
    if count >= 1 :
        break
    else: m += 1

print(m, count, sep="\n")


