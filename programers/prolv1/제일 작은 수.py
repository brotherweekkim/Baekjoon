def solution(arr):
    answer = []
    min_num = min(arr)
    for i in arr:
        if i == min_num:
            continue
        answer.append(i)
    return answer if answer else [-1]