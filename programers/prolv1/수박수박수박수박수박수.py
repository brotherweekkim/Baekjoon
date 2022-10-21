def solution(n):
    subak = '수박'
    if n % 2:
        answer = subak * (n // 2) + '수'
    else:
        answer = subak * (n // 2)
    return answer