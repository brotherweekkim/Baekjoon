def solution(nums):
    monsters = set(nums)
    N = len(nums) // 2
    if N > len(monsters):
        return len(monsters)
    return N