def max_d(n, m):
    result = 1
    for i in range(2, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            result = i
    return result
        
def solution(arr):
    answer = arr[0]
    for idx in range(1, len(arr)):
        answer = int(answer * arr[idx] / max_d(answer, arr[idx]))
    return answer