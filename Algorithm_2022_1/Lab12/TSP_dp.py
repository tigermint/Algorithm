def isIn(i, A):
    if (A & (1 << (i - 2)))!= 0:
        return True
    else: 
        return False

def count(A, n):
    count = 0
    for i in range(n):
        if (A & (1 << i)) != 0: 
            count += 1
    return count

def diff(A, j):
    t = 1 << (j - 2)
    return (A & (~t))

def minimum(W, D, i, A):
    minValue = INF
    minJ = 1
    n = len(W) - 1
    for j in range(2, n + 1):
        if isIn(j, A):
            m = W[i][j] + D[j][diff(A, j)]
            if minValue > m:
                minValue = m
                minJ = j
    return minValue, minJ

def travel(W):
    n = len(W) - 1
    size = 2 ** (n - 1)
    D = [[0] * size for _ in range(n + 1)]
    P = [[0] * size for _ in range(n + 1)]
    for i in range(2, n + 1): # direct 경로 초기화
        D[i][0] = W[i][1]
    for k in range(1, n - 1): # A집합 v1, vj 제외 나머지 n-2개 
        for A in range(1, size): # A부분집합 개수가 1 ~ n-2개 각 vertex 확인
            if count(A, n) == k:
                for i in range(2, n + 1):
                    if(not isIn(i, A)): # A 집합에 속하지 않는 i 찾고
                        D[i][A], P[i][A] = minimum(W, D, i , A) # 최소값 구하고 Path return

    A = size - 1
    D[1][A], P[1][A] = minimum(W, D, 1, A)
    return D, P

def tour(v, A, P):
    k = P[v][A]
    if A == 0:
        print(1)
    else:
        print(k, end=" ")
        tour(k, diff(A, k), P)

# input
INF = 99
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


# output
D, P = travel(W)
print(D[1][2**(len(W) - 2) -1]) # 경로 값
# 최적 경로
print(1, end=" ")
tour(1, 2**(n - 1)-1, P)
# D 테이블
for i in range(1, len(D)):
    for j in range(len(D[i])):
        if (D[i][j] != INF) and (D[i][j] != 0):
            print(i, j, D[i][j], sep= " ")

