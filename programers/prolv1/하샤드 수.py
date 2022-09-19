def solution(x):
    num = 0
    for i in str(x):
        num += int(i)
    return not bool(x % num)