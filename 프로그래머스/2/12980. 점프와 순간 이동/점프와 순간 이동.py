# K 칸 앞으로, 전지 K 감소
# 현재까지 온 거리 * 2 순간 이동
# 건전지 사용량 줄이기 위해 점프 최소
# N 주어졌을 때 사용량 최소 return

def solution(n):
    ans = 0
    while n:
        if n % 2 == 0:
            n /= 2
        else:
            n = (n - 1) / 2
            ans += 1
    return ans