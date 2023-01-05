'''
https://softeer.ai/practice/info.do?idx=1&eid=395&sw_prbl_sbms_sn=119283
난이도 별 2개
'''

dic = {}
W, N = map(int, input().split())
answer = 0
for _ in range(N):
    M, P = map(int, input().split())
    m = dic.get(P, 0) + M
    dic[P] = m

p_list = sorted(dic.keys(), reverse = True)
for i in p_list:
    if W >= dic[i]:
        W -= dic[i]
        answer += dic[i] * i
    else:
        answer += W * i
        break

print(answer)