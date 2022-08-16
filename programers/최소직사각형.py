def solution(sizes):
    w = 0
    h = 0
    for size in sizes:
        if w < min(size):
            w = min(size)
        if h < max(size):
            h = max(size)
    return w * h