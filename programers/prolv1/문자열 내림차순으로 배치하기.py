def solution(s):
    tolist = list(s)
    tolist.sort(reverse = True)
    return ''.join(tolist)