# 백준 1978 소수 찾기
def findPrimeNum(num):
    if num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
            

# input
n = int(input())
nums = list(map(int, input().split()))
count = 0
for num in nums:
    if findPrimeNum(num):
        count += 1
print(count)