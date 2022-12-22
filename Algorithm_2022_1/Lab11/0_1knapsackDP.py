def knapsack(n, w, W, p, P):
    if n <= 0 or W <= 0:
        return 0
    if w[n] > W: # 현재 무게가 W를 초과해 버리는 경우
        value = knapsack(n - 1, w, W, p, P) # 이전 노드 까지가 maxProfit
        tmp = [n, W, value] # n : 사용된 item 개수, W : 현재 채울 수 있는 무게, value : 현재까지의 profit
        if tmp not in P:
            P.append(tmp)
        return value
    else:        
        left = knapsack(n - 1, w, W, p, P) # w가 포함 안될 경우        
        right = knapsack(n - 1, w, W - w[n], p, P) # w가 포함 될 경우
        result = max(left, p[n] + right)       
        tmp = [n, W, result]
        if tmp not in P:
            P.append(tmp)  
        return result


# input
n = int(input()) # 아이템 개수
w = list(map(int, input().split())) # 각 아이템 무게
p = list(map(int, input().split())) # 각 아이템 profit

# 단위 무게 별로 내림차순 정렬 -> 정렬 안해도 답은 나온다 -> 넣는 순서가 다른 것
for i in range(n):
    for j in range(i, n):
        if (p[i] / w[i]) < (p[j]/w[j]):
            tmp = p[i]; p[i] = p[j]; p[j] = tmp
            tmp = w[i]; w[i] = w[j]; w[j] = tmp

#index를 위해 맨 앞 0 삽입
w.insert(0, 0)
p.insert(0, 0)

T = int(input()) # 배낭 개수
W = [int(input()) for _ in range(T)] # 배낭마다 최대 무게

for i in range(T):
    P = list() # 해당하는 아이템 조합 저장하고 x[0], x[1] 기준 sort해서 출력
    print(knapsack(n, w, W[i], p, P))
    P.sort(key=lambda x: (x[0], x[1]))
    for i in P:
        print(" ".join(map(str, i)), end="\n")

