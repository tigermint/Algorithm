from queue import PriorityQueue

class SSTNode:
    
    def __init__ (self, level): # 노드 생성자
        self.level = level
        self.path = []
        self.bound = 0

    def __lt__(self, other): # bound 비교값
        return self.bound < other.bound        

    def contains(self, x): # path에 x가 포함되어 있다면 true, 아니면 false  
        for i in range(len(self.path)):
            if (self.path[i] == x):
                return True
        return False    

    def print(self):
        if self.bound >= 999:
            print(str(self.level) + " INF " + " ".join(map(str, self.path)), end="\n")
        else:
            print(self.level, self.bound, " ".join(map(str, self.path)), end="\n")

def hasOutgoing(v, path):
    for i in range(0, len(path) - 1): # 처음부터 path - 1 까지 check
        if path[i] == v:
            return True
    return False 

def hasIncoming(v, path):
    for i in range(1, len(path)): # 1부터 path 끝까지
        if (path[i] == v):
            return True
    return False

def length(path, W):
    total = 0
    prev = 1
    for i in range(len(path)):
        if (i != 0):
            prev = path[i - 1]
        total += W[prev][path[i]] 
        prev = path[i]
    return total

def bound(v, W):
    n = len(W) - 1
    total = length(v.path, W) # 이미 지나온 path들 +
    for i in range(1, n + 1):
        if (hasOutgoing(i, v.path)): # 이미 path에 포함되어 떠난 노드들이면 제거
            continue
        min = INF
        for j in range(1, n + 1):
            if (i == j): # self loop 제거
                continue
            if (hasIncoming(j, v.path)): # v-path 에 들어오는 edge가 있으면 제거
                continue
            if (j == 1 and i == v.path[len(v.path) - 1]): # v.path에서 마지막 노드에서 1로 가는 경로가 있으면 제거
                continue
            if (min > W[i][j]): # 최소 업데이트
                min = W[i][j]
        total += min
    return total
    
def travel2 (W):
    global minlength, opttour
    n = len(W) - 1
    PQ = PriorityQueue()
    v = SSTNode(0) # 파라미터 level
    v.path = [1] # 첫번째 노드 1번 노드 추가
    v.bound = bound(v, W)
    v.print()
    minlength = INF
    PQ.put((v.bound, v)) # v.bound기준으로 v 추가
    while (not PQ.empty()): # 큐가 빌 때 까지
        v = PQ.get()[1] # 가장 우선순위 v가져온다
        if (v.bound < minlength): # 하한이 현재의 최소 길이보다 작다면 고려 대상 (pruning)
            for i in range(2, n + 1): 
                if (v.contains(i)): # i가 path에 포함되어 있는 경우 거르기
                    continue
                u = SSTNode(v.level + 1) # level 한단계 확장 
                u.path = v.path[:] # deep copy, 전 level노드 path 넣어준다.
                u.path.append(i) 
                if (u.level == n - 2): # level이 n -2 라면 leaf node
                    for k in range(2, n + 1): # 포함되어 있지 않은 노드 찾아서 append 해준다 중요******
                        if (not u.contains(k)):
                            u.path.append(k)
                    u.path.append(1) # 마지막 원래로 돌아가는 첫번째 노드 중요*********
                   
                    u.print()
                    if (length(u.path, W) < minlength): # path 완성되면 minlength update
                        minlength = length(u.path, W)
                        opttour = u.path[:]
                else:
                    u.bound = bound(u, W) # leaf node가 아니라면 bound 계산
                    u.print()
                    if (u.bound < minlength): # push 해주기
                        PQ.put((u.bound, u))




# input
INF = 999
n, m = map(int, input().split(" "))

W = [[-1 for _ in range(n + 1)] for _ in range(n + 1 )] # 0, 1, 2, 3 ... n 

for _ in range(m):
    u, v, w = map(int, input().split())
    W[u][v] = w

for i in range(1, n + 1):
    W[i][i] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if W[i][j] == -1:
            W[i][j] = INF

minlength = INF
opttour = None
travel2(W)
print(minlength)
print(opttour)