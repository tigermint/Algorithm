N, M = list(map(int, input().split()))  # length
J = int(input())
moves = [int(input()) - 1 for _ in range(J)]  # index
index = [0, M - 1]  # index
result = 0

for move in moves:
    if index[0] > move:
        # 왼쪽으로 이동할 경우
        result += index[0] - move
        index[0], index[1] = move, move + M - 1
    elif index[1] < move:
        # 오른쪽으로 이동할 경우
        result += move - index[1]
        index[0], index[1] = move - M + 1, move

print(result)