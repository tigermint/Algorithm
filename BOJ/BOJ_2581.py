# 소수 - 에라토스테네스의 체
import math
def seive(M, N): # M ~ N 사이 소수들의 합
    global count
    count = 0
    flags = [0, 0] + [1]*(N-1)
    sqrtn= math.floor(math.sqrt(N))
    for i in range(2, sqrtn + 1):
        if flags[i] == 1:
            for j in range(2*i, N + 1, i):
                flags[j] = 0
    sum = 0
    minPrime = N + 2
    for i in range(M, N + 1):
        if flags[i] == 1: 
            sum+=i
            if minPrime > i:
                minPrime = i
    if sum == 0: print(-1)
    else: print(sum, minPrime, sep="\n")

# input
M = int(input())
N = int(input())
seive(M, N)