import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

A.sort()

for m in m_list:
    check = False
    start, end = 0, N - 1
    while start <= end:
        mid = (end + start)//2
        if A[mid] == m:
            check = True
            break

        if m < A[mid]:
            end = mid - 1
        elif m > A[mid]:
            start = mid + 1
    if check:
        print(1)
    else:
        print(0)
