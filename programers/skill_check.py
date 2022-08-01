# 최대 공약수 구하기
def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

def LCM(x, y):
    result = (x * y) // GCD(x, y)
    return result

def solution(arr):
    answer = 1
    for i in arr:
        answer = LCM(answer, i)
    return answer