import itertools 

def solution(relation):
    col_len = len(relation[0])
    col_idx = [i for i in range(col_len)] # 나와야할 조합, 갱신 시 조합으로 뽑는다
    answer_idx = []
    for s in range(1, col_len + 1): # 개수
        rotate = list(zip(*relation))
        
        data = []
        data_idx = []
        for combi in itertools.combinations(col_idx, s):
            data.append([rotate[c] for c in combi])
            data_idx.append(combi)
        
        merged_data = []
        for sublist in data:
                merged_tuple = tuple(''.join(sub) for sub in zip(*sublist))
                merged_data.append(merged_tuple)
        
        tmp_idx = []
        # # 컬럼 순서 조합
        for idx in range(len(data_idx)):
            # 같으면 식별 가능한 조합
            if len(merged_data[idx]) == len(set(merged_data[idx])):
                # 최소성 판별
                check = -1
                for ai in answer_idx:
                    if set(ai).issubset(set(data_idx[idx])): # 부분 집합
                        check = 0
                        break
                if check == -1:
                    answer_idx.append(list(data_idx[idx]))
    return len(answer_idx)

