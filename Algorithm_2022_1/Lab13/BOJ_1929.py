# 백준 1929 소수 구하기 -> 에라토스테네스의 체
import math
def sieve(M, N):
    global count
    count = 0
    flags = [0, 0] + [1] * (N - 1) # 0 0 1 1 1 1 ... n + 1개
    sqrtn = math.floor(math.sqrt(N)) # math.floor 내림, math.ceil 올림, 2에서 루트 n까지 소수 판별하면 뒤의 n까지는 판별된다.
    for i in range(2, sqrtn + 1): # 2부터 시작해서 2,3,4, ... 1이면 그 배수를 모두 소수가 아니다 판별하고 0으로 바꿔준다
        if flags[i] == 1: 
            for j in range(2 * i, N + 1, i): # 배수 확장 -> 1로 교체
                flags[j] = 0
    primes = []
    for i in range(M, len(flags)):
        if flags[i] == 1:
            primes.append(i)
            count += 1
    return primes
            
# input
M, N = map(int, input().split())
count = 0

for prime in sieve(M, N):
    
    print(prime)


print(count)
