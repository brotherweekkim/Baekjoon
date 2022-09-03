def solution(n):
    if n % 2:
        return 2
    
    for i in range(3, int((n - 1) ** (1/2)) + 1):
        if (n - 1) % i == 0:
            return i
    
    return n - 1