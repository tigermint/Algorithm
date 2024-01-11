def solution(people, limit):
    answer = 0
    people.sort()
    # 50 50 70 80
    i, j = 0, len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        answer += 1
    return answer