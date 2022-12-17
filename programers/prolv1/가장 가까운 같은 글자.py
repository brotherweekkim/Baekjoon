def solution(s):
    answer = []
    dic = {}
    for idx, a in enumerate(s):
        if dic.get(a) or dic.get(a) == 0:
            answer.append(idx - dic[a])
            dic[a] = idx
        else:
            answer.append(-1)
            dic[a] = idx
    return answer