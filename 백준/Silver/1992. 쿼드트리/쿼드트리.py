def compression(matrix):
    # 종료 조건
    if all(element == matrix[0][0] for row in matrix for element in row):
        return str(matrix[0][0])

    # 크기가 1x1인 행렬
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return str(matrix[0][0])

    # 재귀 조건
    mid = len(matrix) // 2
    top_left = [row[:mid] for row in matrix[:mid]]
    top_right = [row[mid:] for row in matrix[:mid]]
    bottom_left = [row[:mid] for row in matrix[mid:]]
    bottom_right = [row[mid:] for row in matrix[mid:]]

    return (
        "("
        + compression(top_left)
        + compression(top_right)
        + compression(bottom_left)
        + compression(bottom_right)
        + ")"
    )


N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
print(compression(matrix))
