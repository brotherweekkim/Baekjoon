def solution(arr, divisor):
    arr.sort()
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    if answer == []:
        return [-1]
    return answer