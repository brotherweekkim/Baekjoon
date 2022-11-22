def solution(n):
    answer = 0
    memo = [0] * 2001
    memo[1] = 1
    memo[2] = 2
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n] % 1234567