# input
N = int(input())
times = []

for _ in range(N):
    s, e = list(map(int, input().split()))
    times.append([s, e])

times.sort(key = lambda x: x[0])
times.sort(key = lambda x: x[1])

[count, cmp] = [1, times[0][1]]

times.pop(0);

for time in times:
    if time[0] >= cmp:
        count += 1
        cmp = time[1]
print(count)

