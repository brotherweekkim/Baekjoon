def binery(num):
    result = ''
    while num > 1:
        result = str(num % 2) + result
        num //= 2
    return '1' + result

def solution(s):
    answer = [0, 0]
    while len(s) != 1:
        answer[0] += 1
        answer[1] += s.count('0')
        s = binery(s.count('1'))
    return answer