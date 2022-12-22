def knapsack(i, profit, weight):
    global maxProfit, numBest, bestSet
    # maxProfit 갱신    
    if weight <= W and profit > maxProfit:
        maxProfit = profit
        numBest = i
        bestSet = include[:]
    if promising(i, profit, weight): 
        include[i + 1] = True
        knapsack(i + 1, profit + p[i + 1], weight + w[i + 1])
        
        include[i + 1] = False
        knapsack(i + 1, profit, weight)
        

def promising(i, profit, weight):
    global bound

    if weight > W: # pruning 전략 - 현재 weight가 W를 넘어버리면 pruning
        print(i, weight, profit,int(bound),maxProfit, end=" ")
        print("다음 vertex 접근 불가능 - 가능 무게를 초과하였습니다")  
        return False
    else: # pruning 전략 - bound <= maxProfit 이면 pruning
        # bound는 지금까지 담은 무게에 남은 무게를 fraction 해서 채운 profit이다. 즉 지금 현재 상황에서의 최대이익 -> Greedy하게 구한 것
        j = i + 1 # j 다음 item
        bound = profit
        totoweight = weight
        while (j <= n) and (totoweight+ w[j] <= W): # 남은 아이템이 있고, 지금까지 weight에서 다음 아이템 무게를 더할 시 < W이면        
            totoweight += w[j] # 다음 아이템을 넣어줌
            bound += p[j] # bound에 다음 아이템 profit을 넣어줌
            j += 1          
        k = j # 무게가 넘어가는 즉 while문 빠져나온 fraction 해야하는 아이템의 index
        if k <= n: # 그 아이템이 마지막 아이템 인덱스 보다 작다면
            bound += (W -totoweight) * p[k] / w[k] # fraction해서 채워준다   
        print(i, weight, profit, int(bound), maxProfit, end=" ")
        if bound > maxProfit: 
            print("다음 vertex 접근 가능") 
            return True
        else: 
            print("다음 vertex 접근 불가능 - bound <= maxProfit") 
            return False

        #return bound > maxProfit # bound 즉 상한이 maxProfit 보다 커야 다음 아이템을 넣어 줄 만함
    

#print(i, weight,bound, profit,maxProfit)


# input
n, W = map(int, input().split())
w = list(map(int, input().split(" ")))
p = list(map(int, input().split(" ")))

# 내림차순으로 정렬 -> Greedy하게 profit을 탐하기 위해 
for i in range(n):
    for j in range(i, n):
        if (p[i] / w[i]) <= (p[j]/w[j]):
            tmp = p[i]; p[i] = p[j]; p[j] = tmp
            tmp = w[i]; w[i] = w[j]; w[j] = tmp

# index 맞추기 위한 가장 앞 0 삽입
w.insert(0, 0)
p.insert(0, 0)

maxProfit = 0
numBest = 0
bestSet = []
include = [False] * (n + 1)
bound = 0

print("\n접근 vertex :")
knapsack(0, 0, 0)

print(maxProfit)
for i in range(len(bestSet)):
    if bestSet[i] == True:
        print(w[i], p[i], sep=" ")

