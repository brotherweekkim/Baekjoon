def solution(n):
    answer = sorted(list(str(n)), reverse = True)
    return int(''.join(s for s in answer))