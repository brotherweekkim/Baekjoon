from operator import itemgetter
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
arr.sort(key=itemgetter(1,0))
for i in range(N):
    print(*arr[i])