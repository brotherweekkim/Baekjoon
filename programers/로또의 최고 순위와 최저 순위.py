def solution(lottos, win_nums):
    answer = []
    right = 0
    unknown = 0
    for lotto in lottos:
        if lotto:
            if lotto in win_nums:
                right += 1
        else:
            unknown += 1
    answer.append(7 - (right + unknown) if right + unknown else 6)
    answer.append(7 - right if right else 6)
    return answer