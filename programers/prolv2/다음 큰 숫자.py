def binary(num):
    result = ''
    while num != 1:
        result = str(num % 2) + result
        num //= 2
    return '1' + result

def solution(n):
    one_cnt = binary(n).count('1')
    while True:
        n += 1
        if one_cnt == binary(n).count('1'):
            break
    return n