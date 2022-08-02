def solution(prices):
    answer = []
    N = len(prices)
    for i in range(N):
        cnt = 0
        for j in range(i + 1, N):
            cnt += 1
            if prices[i] > prices[j]:
                break
            
        answer.append(cnt)
    return answer