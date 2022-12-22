def sumOfSubsets(i, weight, total):
    global count
    if promising(i, weight, total):
        if weight == W: # solution
            count += 1
            subset = []
            for k in range(1, n + 1):
                if include[k] == True:
                    subset.append(w[k])
            solutionSubset.append(subset)
        else: # 다음 노드로
            include[i + 1] = True
            sumOfSubsets(i + 1, weight + w[i + 1], total - w[i + 1])
            include[i + 1] = False
            sumOfSubsets(i + 1, weight, total - w[i + 1])

def promising(i, weight, total):
    return (weight + total >= W) and (weight == W or weight + w[i + 1] <= W)

#input
n, W = map(int, input().split())
w = list(map(int, input().split()))
include = [False for _ in range(n + 1)]

w.insert(0, 0)

weight = 0 # 현재 무게
total = sum(w) # 남은 무게

count = 0
solutionSubset = []

sumOfSubsets(0,weight, total)

#output
print(count)
for i in range(0, count):
    print(" ".join(map(str, solutionSubset[i])))
