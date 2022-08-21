def solution(N, stages):
    answer = [i for i in range(1, N + 1)]
    passed_stages = {}
    failed_stages = {}
    
    for i in range(1, N + 1):
        passed_stages[i] = 0
        failed_stages[i] = 0
        
    for stage in stages:
        for s in range(1, stage):
            passed_stages[s] += 1
        if stage > N:
            continue
        failed_stages[stage] += 1
    
    answer.sort(key = lambda x: failed_stages[x]/(passed_stages[x] if passed_stages[x] else 1), reverse = True)
    return answer