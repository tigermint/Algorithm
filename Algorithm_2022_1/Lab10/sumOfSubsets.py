def sumOfSubsets(i, weight, total):
    global count
    global allSubset
    n = len(w) - 1
    if promising(i, weight, total):
        if weight == W:
            count += 1
            subset = []
            for i in range(1, n + 1):
                if include[i] == True: 
                    subset.append(w[i])
            allSubset.append(subset)
        else:
            include[i + 1] = True # 왼쪽 서브트리
            sumOfSubsets(i + 1, weight + w[i + 1], total - w[i + 1]) # 해당 원소 포함이니 지금가지의 weight에 다음 레벨 weight 포함, total 무게에서는 빼주기
            include[i + 1] = False
            sumOfSubsets(i + 1, weight, total - w[i + 1]) # 지금까지의 weight에 포함되지 않음.

def promising(i, weight, total):
    # 전략 1 : 오름차순으로 정렬되었기 때문에 i의 weight < i + 1의 weight
    # 현재까지 탐색한 노드들의 총 weight의 합이 이미 구하려는 값 W보다 크다면 ? pruning되어야 한다.
    # 전략 2 : 현재까지 탐색한 노드들의 weight들을 제외한 남은 weight들을 모두 더했을 경우 W보다 작다면 ? 남은 노드 탐색해도 W에 도달할 가능성 없음. -> pruning
    if ((weight + total) >= W) and ((weight == W) or (weight + w[i + 1] <= W)):
        return True
    else:
        return False

n, W = map(int, input().split(" ")) # n weight 원소 개수 W = 목표 무게
w = list(map(int, input().split(" "))) # 무게 list
w.insert(0, 0) # index 맞추기 위해 0, 1, 2, 3, 4, weight는 오름차순으로 정렬되어 들어온다. -> input값 정렬하기

total = sum(w) # 앞으로 추가할 수 있는 무게 처음은 root가 0이기 때문에 총 무게겠지 ?
include = [False] * (n + 1) # 해당 원소의 포함 여부
allSubset = [] # 발견한 모든 부분집합 저장
count = 0 # 개수

sumOfSubsets(0, 0, total)
print("가능 개수: " + str(count))
for i in range(count):
    print("부분 집합 : " + " ".join(map(str, allSubset[i])))


