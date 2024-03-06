def time_to_sec(time):
    return time[1] + time[0] * 60


def sec_to_time(s):
    return [s // 60, s % 60]


N = int(input())
# 48분 동안 지속
goals = list(
    map(
        lambda x: [x[0], time_to_sec(list(map(int, x[1].split(":"))))],
        [list(map(str, input().split())) for _ in range(N)],
    )
)

score = [0, 0]  # 바뀌는 시점 인지해야함
team1, team2 = [0, 0]  # 초

for i in range(0, len(goals)):
    if score[0] != 0 or score[1] != 0:  # 0:0 무시
        if score[0] > score[1]:  # 1팀 이기고 있는 경우
            team1 += goals[i][1] - goals[i - 1][1]
        elif score[0] < score[1]:
            team2 += goals[i][1] - goals[i - 1][1]

    # 점수 업데이트
    score[int(goals[i][0]) - 1] += 1

# 마지막 값 업데이트
if score[0] > score[1]:
    team1 += 48 * 60 - goals[-1][1]
elif score[0] < score[1]:
    team2 += 48 * 60 - goals[-1][1]

# 분/초 수정
team1, team2 = [sec_to_time(team1), sec_to_time(team2)]
print(
    f"{team1[0] if team1[0] >= 10 else '0' + str(team1[0])}:{team1[1] if team1[1] >= 10 else '0' + str(team1[1])}"
)
print(
    f"{team2[0] if team2[0] >= 10 else '0' + str(team2[0])}:{team2[1] if team2[1] >= 10 else '0' + str(team2[1])}"
)
