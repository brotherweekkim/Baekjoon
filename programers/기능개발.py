from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    while progresses:
        num = len(progresses)
        cnt = 0
        
        for i in range(num):
            progresses[i] += speeds[i]
            
        for i in range(num):
            if progresses[i] < 100:
                break
            cnt += 1
            
        if cnt:
            for i in range(cnt):
                progresses.popleft()
                speeds.popleft()
            answer.append(cnt)
    
    return answer