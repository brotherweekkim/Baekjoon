def solution(brown, yellow):
    w = h = 0
    for i in range(2, brown // 2):
        h = i
        w = brown // 2 - h
        if (h - 1) * (w - 1) == yellow:
            break
    
    return [w + 1, h + 1]