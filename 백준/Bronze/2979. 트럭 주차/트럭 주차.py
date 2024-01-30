fee = list(map(int, input().split(' ')))
arr = []
for _ in range(3):
    arr.append(list(map(int, input().split(' '))))
rot = list(zip(*arr))
start, end = min(rot[0]), max(rot[1])

answer = 0
for time in range(start, end + 1):
    count = 0
    for i in range(3):
        if arr[i][0] <= time < arr[i][1]:
            count += 1
    answer += fee[count - 1] * count
print(answer)