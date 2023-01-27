import sys
input = sys.stdin.readline

# 가장 많은 보석을 가져간 학생의 보석이 최소가 되게, 없는거도 가능, 한 학생은 한가지색 보석
N, M = map(int, input().split())  # 학생, 보석 색상 수
gems = [int(input()) for _ in range(M)]

left = 1
right = max(gems)
result = right
while left <= right:
    mid = (left + right) // 2

    person = 0
    for gem in gems:
        person += gem // mid
        if gem % mid > 0:
            person += 1
    if person > N:
        left = mid + 1
    else:
        result = min(result, mid)
        right = mid - 1
print(result)
