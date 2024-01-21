def intersection(set1, set2):
    result = []
    set2_copy = set2.copy()
    for i in set1:
        if i in set2_copy:
            set2_copy.remove(i)
            result.append(i)
    return len(result)

def union(set1, set2):
    return len(set1) + len(set2) - intersection(set1, set2)

def solution(str1, str2):
    set1, set2 = [], []
    for i in range(len(str1) - 1):
        tmp = str1[i:i+2].lower()
        if tmp.isalpha():
            set1.append(tmp)
    for i in range(len(str2) - 1):
        tmp = str2[i:i+2].lower()
        if tmp.isalpha():
            set2.append(tmp)
            
    if not set1 and not set2:
        return 65536
    return int((intersection(set1, set2) / union(set1, set2)) * 65536)
