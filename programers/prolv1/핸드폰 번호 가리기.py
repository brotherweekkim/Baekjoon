def solution(phone_number):
    n = len(phone_number)
    star = '*' * (n - 4)
    back_number = phone_number[n - 4:]
    answer = star + back_number
    return answer