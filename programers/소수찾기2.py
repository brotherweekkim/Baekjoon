from itertools import permutations

def is_prime_number(num):
    if num == 0 or num == 1:
        return 0
    for i in range(2, int((num) ** (1/2)) + 1):
        if num % i == 0:
            return 0
    return 1

def solution(numbers):
    answer = set()
    per = []
    for i in range(1, len(numbers) + 1):
        per += list(permutations(numbers, i))
        
    for p in per:
        new = int("".join(p))
        if is_prime_number(new):
            answer.add(new)

    return len(answer)