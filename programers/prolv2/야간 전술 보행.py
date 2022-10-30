def solution(distance, scope, times):
    answer = 0
    road = {}

    for idx, s in enumerate(scope):
        for p in range(min(s), max(s) + 1):
            road[p] = idx
            
    for d in range(1, distance + 1):
        guard = road.get(d, -1)
        if guard != -1:
            if 0 < d % (times[guard][0] + times[guard][1]) <= times[guard][0]:
                return d
    return distance