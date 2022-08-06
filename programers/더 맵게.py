import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
            break
        sweet_food = heapq.heappop(scoville)
        sweet_food2 = heapq.heappop(scoville)
        heapq.heappush(scoville, sweet_food + sweet_food2 * 2)
        answer += 1
        
        
    return answer