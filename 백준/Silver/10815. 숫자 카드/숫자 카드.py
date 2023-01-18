N = int(input())
nums = list(map(int, input().split()))
M = int(input())
tests = list(map(int, input().split()))

d = {}
for num in nums: d[num] = 0

for test in tests:
    print(1, end=" ") if test in d else print(0, end=" ")
print()