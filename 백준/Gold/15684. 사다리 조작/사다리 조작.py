def check():
    for sj in range(1, N + 1):  # 모든 sj 값이 끝날 때도 같아야 성공
        j = sj
        for i in range(1, H + 1):
            if arr[i][j] == 1:  # 오른쪽으로 이동
                j += 1
            elif arr[i][j - 1] == 1:  # 왼쪽으로 이동
                j -= 1
        if j != sj:
            return 0
    return 1


def dfs(n, s):
    global ans
    if ans == 1:  # 가지치기
        return

    if n == cnt:  # 모든 개수를 선택 완료
        if check() == 1:
            ans = 1
        return

    for j in range(s, CNT):
        ti, tj = pos[j]
        # 왼/오 둘다 사다리 아니면 가능
        if arr[ti][tj - 1] == 0 and arr[ti][tj + 1] == 0:
            arr[ti][tj] = 1
            dfs(n + 1, j + 1)
            arr[ti][tj] = 0


N, M, H = list(map(int, input().split()))

# [1] 사다리 입력 받기 (문제 좌표와 직관적으로 일치)
arr = [[0] * (N + 2) for _ in range(H + 1)]
for _ in range(M):
    ti, tj = map(int, input().split())  # 미리 놓아져 있는 사다리
    arr[ti][tj] = 1  # 사다리 있는 좌표

# [2] 사다리 놓을 후보 저장
pos = []
for i in range(1, H + 1):
    for j in range(1, N + 1):
        if arr[i][j] == 0:  # 사다리 놓을 수 있는 곳
            pos.append((i, j))
CNT = len(pos)

# [3] 추가하는 사다리 개수 0 ~ 3 실행 => 안되면 -1이 정답
for cnt in range(4):
    ans = 0
    dfs(0, 0)  # CNT개에서 cnt개수를 뽑는 모든 조합
    if ans == 1:
        ans = cnt
        break
else:  # 발견하지 못했다면 break 안했음
    ans = -1
print(ans)
