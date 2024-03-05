H, W = list(map(int, input().split()))
matrix = [list(map(str, input())) for _ in range(H)]
result = [[-1 for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if matrix[i][j] == "c":
            result[i][j] = 0
        else:
            try:
                result[i][j] = (
                    j - list(filter(lambda x: matrix[i][x] == "c", range(0, j)))[-1]
                )
            except:
                pass

for i in range(H):
    for j in range(W):
        print(result[i][j], end=" ")
    print()
