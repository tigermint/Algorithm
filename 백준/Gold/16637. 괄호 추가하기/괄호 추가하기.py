# 0.5초
# 연산자 우선순위 동일
# 괄호 있음, 중첩 괄호 사용 불가 -> 괄호 적절히 추가해서 결괏값 최대
# 식의 결과의 최댓값
# 연산자는 +, -, * 중 하나


def cal(a, b, operator):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b


def dfs(index, target):
    global result
    if index == N - 1:
        result = max(result, target)

    if index + 2 < N:  # 다음 연산이 괄호가 없는 경우
        dfs(
            index + 2,
            cal(target, math_expression[index + 2], math_expression[index + 1]),
        )
    if index + 4 < N:  # 다음 연산이 괄호가 있는 경우
        dfs(
            index + 4,
            cal(
                target,
                cal(
                    math_expression[index + 2],
                    math_expression[index + 4],
                    math_expression[index + 3],
                ),
                math_expression[index + 1],
            ),
        )


N = int(input())
math_expression = list(input())
result = -pow(2, 31)

# 숫자 변환
for i in range(0, len(math_expression), 2):
    math_expression[i] = int(math_expression[i])
dfs(0, math_expression[0])
print(result)
