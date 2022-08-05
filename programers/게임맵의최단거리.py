from collections import deque

def solution(maps):
    answer = 0
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n = len(maps)
    m = len(maps[0])
    root = deque()
    root.append((0, 0))
    while root:
        r, c = root.popleft()
        for dr, dc in d:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if maps[nr][nc] == 1:
                maps[nr][nc] = maps[r][c] + 1
                root.append((nr, nc))
                
    if maps[n - 1][m - 1] == 1:
        answer = -1
        
    else:
        answer = maps[n - 1][m - 1]
    return answer
