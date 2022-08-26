def solution(numbers):
    all_numbers = {1,2,3,4,5,6,7,8,9}
    answer = sum(all_numbers - set(numbers))
    return answer