def find(N, k):
    digit = 0 # 자리 수
    num = 0  # 그 전자리 까지 총 숫자
    while num < k:
        digit += 1
        num += 9 * pow(10, digit - 1) * (digit)
    
    k -= num
    count = k // 10
    rest = k % 10
    return count, num
    



# input
N, k = list(map(int, input().split()))
print(find(N, k))








