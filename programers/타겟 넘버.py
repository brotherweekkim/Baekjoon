answer = 0

def DFS(n, numbers, target):
    global answer
    
    if n == len(numbers):
        if sum(numbers) == target:
            answer += 1
            
        return
    
    numbers[n] *= -1
    DFS(n + 1, numbers, target)
    numbers[n] *= -1
    DFS(n + 1, numbers, target)
    
    
def solution(numbers, target):
    global answer
    DFS(0, numbers, target)
    
    return answer