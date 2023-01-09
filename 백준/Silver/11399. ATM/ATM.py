n = int(input())
time_list = list(map(int, input().split()))
min_list = []; s = 0
time_list.sort()
for i in range(0, n):
    s += time_list[i]
    min_list.append(s)
print(sum(min_list))