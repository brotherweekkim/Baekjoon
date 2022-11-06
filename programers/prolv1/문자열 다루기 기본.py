def solution(s):
    answer = True
    num_arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(s) != 4 and len(s) != 6:
        return False
    for i in s:
        if i not in num_arr:
            return False
    return answer