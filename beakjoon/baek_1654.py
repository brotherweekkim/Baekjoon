K, N = map(int, input().split())
cables = []
for i in range(K):
    cables.append(int(input()))
e = max(cables)
s = 1
while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for cable in cables:
        cnt += cable // mid
    if cnt >= N:
        s = mid + 1
    else:
        e = mid - 1
print(e)