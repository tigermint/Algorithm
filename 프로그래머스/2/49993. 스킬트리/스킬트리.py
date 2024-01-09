def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        check = []
        for st in skill_tree:
            if st in skill and not set(skill[:skill.find(st)]).issubset(set(check)):
                break
            check.append(st)
        if len(check) == len(skill_tree):
            answer += 1
    return answer