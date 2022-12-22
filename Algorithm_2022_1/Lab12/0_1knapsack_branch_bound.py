from queue import PriorityQueue
class SSTNode:
    def __init__(self, level, profit, weight):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = 0

    def __lt__(self, other): # bound 비교값
        return self.bound < other.bound  

    def print(self):
        print(self.level, self.weight, self.profit, int(self.bound))

def knapsack(p, w, W):
    PQ = PriorityQueue()
    v = SSTNode(0, 0, 0)
    maxProfit = 0
    v.bound = bound(v, p, w)
    PQ.put((-v.bound, v)) # 한계값이 큰 순서로 정렬하기 위해 한계값이 클 수록 가능 기대치가 크다
    v.print()
    while(not PQ.empty()):

        v = PQ.get()[1] # PQ의 첫번째 꺼 탐색
        if v.bound > maxProfit: # pruning -> 노드를 탐색하는 도중 계속 maxProfit이 바뀌니깐 마디가 아직 유망한지 검사
            level = v.level + 1
            weight = v.weight + w[level]
            profit = v.profit + p[level]
            u = SSTNode(level, profit, weight) # 다음 레벨이 추가되었을 경우----
            #무게와 maxProfit 갱신 
            #추가 되지 않을 경우에는 갱신 안해도 된다 -> 부모랑 같으니깐
            if u.weight <= W and u.profit > maxProfit: # pruning 전략
                maxProfit = u.profit # pruning 안걸리고 maxProfit 갱신되면 갱신해주기
            u.bound = bound(u, p, w) # bound 계산
            u.print()    
            if u.bound > maxProfit: # pruning 전략
                PQ.put((-u.bound, u))

            u = SSTNode(level, v.profit, v.weight) #다음 레벨이 추가되지 않은 노드----
            u.bound = bound(u, p, w)
            u.print()
            if u.bound > maxProfit:
                PQ.put((-u.bound, u))
    return maxProfit 

            
def bound(u, p, w):
    n = len(p) - 1
    if u.weight >= W:
        return 0
    else:
        result = u.profit
        j = u.level  + 1
        totweight = u.weight
        while j <= n and totweight + w[j] <= W:
            totweight += w[j]
            result += p[j]
            j += 1
        k = j
        if k <= n:
            result += (W - totweight) * p[k] / w[k]
        return result
# input
n, W = map(int, input().split())

# w = input().split()
# p = input().split()

w = list(map(int, input().split()))
p = list(map(int, input().split()))


for i in range(n):
    for j in range(i, n):
        if (p[i] / w[i]) < (p[j]/ w[j]):
           p[i], p[j] = p[j], p[i]
           w[i], w[j] = w[j], w[i]

w.insert(0, 0)
p.insert(0, 0)

maxProfit = knapsack(p, w, W) # 방문하는 모든 노드 출력
print(maxProfit)