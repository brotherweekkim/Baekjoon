def solution(answers):
    answer = []
    stu1 = [1, 2, 3, 4, 5]
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result1 = 0
    result2 = 0
    result3 = 0
    for i in range(len(answers)):
        if stu1[i % len(stu1)] == answers[i]:
            result1 += 1
        if stu2[i % len(stu2)] == answers[i]:
            result2 += 1
        if stu3[i % len(stu3)] == answers[i]:
            result3 += 1
    result = max(result1, result2, result3)
    if result1 == result:
        answer.append(1)
    if result2 == result:
        answer.append(2)
    if result3 == result:
        answer.append(3)
    return answer