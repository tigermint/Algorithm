def hamilton(i):
    global count
    if promising(i):
        if i == n - 1:
            count += 1       
            allPath.append(vindex[0:-1])     
        else: # 다음 노드 탐색
            for vertex in range(2, n + 1): # 1번 노드는 들어가있으니깐 가능 vertex 찾기
                vindex[i + 1] = vertex # 확실하게 탐색할 노드만 넣어준다
                hamilton(i + 1)


def promising(i):
    # 1. 경로 상 i - 1과 인접해 있는지
    # 2. n - 1번째는 0번째와 인접해 있는지
    # 3. i번째는 이전 노드들 중 하나가 될 수 없다 -> 한번만 거쳐야 하기 때문
    flag = True
    if i == n - 1 and W[vindex[i]][vindex[0]] != 1: # n - 1번째는 0번째와 인접해 있는지
        flag = False
    elif i > 0 and W[vindex[i - 1]][vindex[i]] != 1:  # level 0이 아니고 경로 상 i - 1과 인접해 있는지
        flag = False
    else: # 가장 마지막에 이전까지 기록을 판단하여 반복문 돌리는 점을 없앴다
        flag = True
        j = 1 # 0번째는 당연히 통과, level 1과 그 이후 vertex를 비교해야 한다
        while j < i and flag:
            if vindex[j] == vindex[i]:
                flag = False
            j += 1
    return flag   

#input
n, m = map(int, input().split()) # n 노드 개수, m 인접 노드 개수

W = [[0] * (n + 1) for _ in range(n + 1)] # 인접 행렬,vertex는 1번부터 ~ 니깐 저장을 위한 index 0번째를 추가한다
for _ in range(m):
    a,b = map(int, input().split())
    W[a][b] = 1
    W[b][a] = 1

vindex = [0]*(n) # 경로 저장

count = 0
vindex[0] = 1 # 출발점 1 즉 0번째 level == 1 경로 저장 -> 재귀적으로 돌아가도 탐색한 루트만 저장되기 때문에 상관 ㄴ

allPath = []

hamilton(0)
print(count) # 가능한 경로의 수

for i in range(len(allPath)):
    print(allPath[i])
