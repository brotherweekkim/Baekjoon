from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = []
    for idx, city in enumerate(cities):
        low_city = city.lower()
        if len(cache) < cacheSize:
            if low_city in cache:
                cache.pop(cache.index(low_city))
                cache.append(low_city)
                answer += 1
            else:
                answer += 5
                cache.append(low_city)
            
        else:
            if low_city in cache:
                answer += 1
                cache.pop(cache.index(low_city))
                cache.append(low_city)
            else:
                answer += 5
                if cache:
                    cache.pop(0)
                    cache.append(low_city)
    return answer