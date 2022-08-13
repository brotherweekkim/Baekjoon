answer = 0

def is_prime_num(n):
    for i in range(2, int(n ** (1/2))+1):
        if n % i == 0:
            return 0
    return 1

def pick_three(n, nums, result, idx):
    global answer
    if n == 3:
        answer += is_prime_num(sum(result))
        return
    
    for i in range(idx, len(nums)):
        result.append(nums[i])
        pick_three(n + 1, nums, result, i + 1)
        result.pop()

def solution(nums):
    # answer = 0
    pick_three(0, nums, [], 0)

    return answer