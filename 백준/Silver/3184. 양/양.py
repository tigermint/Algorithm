
R, C = map(int, input().split())
yard = [input() for _ in range(R)]
visited = [[False] * C for _ in range(R)]
need_visited = []
sheep, wolf = 0, 0
cmp_sheep, cmp_wolf = 0, 0
moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]

# 양 늑대 인덱스
for i in range(R):
    for j in range(C):
        if yard[i][j] == 'v' or yard[i][j] == 'o':
            need_visited.append([i, j])
count = len(need_visited) - 1

# 늑대 기준으로 dfs
while need_visited:
    node = need_visited.pop()

    # 이미 접근했던 늑대 or 양 위치일 경우 continue
    if visited[node[0]][node[1]] == False:
        visited[node[0]][node[1]] = True

        # 양, 늑대 check
        if yard[node[0]][node[1]] == 'o':
            cmp_sheep += 1
        if yard[node[0]][node[1]] == 'v':
            cmp_wolf += 1

        # 상하 좌우 append
        for move in moves:
            new_node = [node[0] + move[0], node[1] + move[1]]
            if yard[new_node[0]][new_node[1]] != '#' and new_node[0] >= 0 and new_node[1] >= 0:
                need_visited.append(new_node)

    if len(need_visited) == count:
        if cmp_sheep > cmp_wolf:
            sheep += cmp_sheep
        else:
            wolf += cmp_wolf
        cmp_sheep, cmp_wolf = 0, 0
        count = len(need_visited) - 1
    
print(sheep, wolf)