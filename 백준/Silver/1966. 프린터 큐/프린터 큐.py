test_case = int(input())

for i in range(0, test_case):
    N, M = map(int, input().split()) # 문서 개수, 궁금한 문서 현재 큐
    imp_list = list(map(int, input().split())) # 현재 큐의 중요도    
    index = 0
    out_count = 0
    while True:
        # out 되는 경우
        if imp_list[index] >= max(imp_list):
            imp_list[index] = -1
            out_count += 1
            if index == M:
                print(out_count)
                break;       

        if index == N - 1:
            index = 0
        else: index += 1