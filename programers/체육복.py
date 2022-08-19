def solution(n, lost, reserve):
    answer = 0
    stu_list = [1] * (n + 1)
    for i in lost:
        stu_list[i] = 0
    for i in reserve:
        stu_list[i] += 1
    for num in range(n + 1):
        if stu_list[num]:
            continue
            
        if stu_list[num-1] == 2:
            stu_list[num-1] -= 1
            stu_list[num] += 1
            continue
            
        if num != n and stu_list[num + 1] == 2:
            stu_list[num + 1] -= 1
            stu_list[num] += 1
    for stu in stu_list:
        if stu:
            answer += 1
    
    return answer - 1