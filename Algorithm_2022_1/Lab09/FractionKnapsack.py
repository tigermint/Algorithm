def knapsack(item, theifKnapsack, n):
    result = []
    sum = 0
    # 가능한 kg찾기
    for i in range(n):
        if theifKnapsack > item[i][0]:  # 해당 아이템 다 쓸 수 있을 경우
            theifKnapsack -= item[i][0] # 각 아이템 무게 빼기
            result.append([item[i][0], item[i][0] * item[i][2]]) # 그 아이템 추가
            sum += result[i][1] # 해당 아이템 이익 추가
        else:  # 일부만 쓸 경우
            result.append([theifKnapsack, theifKnapsack * item[i][2]]) # 딱맞는 경우를 다 앞에서 다 뺐으니깐 남은무게에다 단위무게만 곱해주면 된다.
            sum += result[i][1] # 해당 아이템 이익 추가
            break
    print(sum)
    for i in range(len(result)):
        print(result[i][0], result[i][1], sep=" ")


# input
n = int(input()) # 아이템 개수
W = list(map(int, input().split(" "))) # 각 아이템 당 무게
profit = list(map(int, input().split(" "))) # 각 아이템 당 profit
unitProfit = list(profit[i] // W[i] for i in range(n)) # 각 아이템 당 단위 무게 -> fraction이기 때문에 단위 무게가 큰 것으로 정렬

item = [[W[i], profit[i], unitProfit[i]] for i in range(n)] # 다 묶어서 [0 : 해당 아이템 무게, 1 : 해당 이익, 2 : 단위 무게]

item.sort(key=lambda x: x[2], reverse=True) # 단위무게를 기준으로 정렬

T = int(input()) # 배낭 개수
theifKnapsacks = [] # 배낭 제한 무게 배열
for _ in range(T):
    theifKnapsacks.append(int(input())) # 배낭 제한 무게

for theifKnapsack in theifKnapsacks: # fraction한 knapsack 최대 이익 구현해보기
    knapsack(item, theifKnapsack, n)