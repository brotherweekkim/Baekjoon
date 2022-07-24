N, r, c = map(int, input().split())
def findZ(N, start, end):
    global r, c  
    if 0 <= c < 2 ** (N - 1):
        # 1구역
        if 0 <= r < 2 ** (N - 1):
            if N == 1:
                return start
            return findZ(N - 1, start, (end + 1)//4 - 1)
        # 3구역
        else:
            r -= 2 ** (N - 1)
            if N == 1:
                return start + 2
            return findZ(N - 1, start + 2 * 2 ** (2 * N - 2), 3 * (end + 1)//4 - 1)
    else:
        # 2구역
        if 0 <= r < 2 ** (N - 1):
            c -= 2 ** (N - 1)
            if N == 1:
                return start + 1
            return findZ(N - 1, start + 2 ** (2 * N - 2), (end + 1)//2 - 1)
            
        # 4구역
        else:
            r -= 2 ** (N - 1)
            c -= 2 ** (N - 1)
            if N == 1:
                return start + 3
            return findZ(N - 1, start + 3 * 2 ** (2 * N - 2), end)

print(findZ(N, 0, (2 ** (N * 2))-1))
