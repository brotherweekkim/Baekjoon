N, M = map(int, input().split())
trees = list(map(int, input().split()))
answer = 0
# 이진탐색을 해보자
start = 1
end = max(trees)

while start <= end:
    mid = (start + end) // 2
        
    sum_trees = 0
    for tree in trees:
        if tree >= mid:
            sum_trees += tree - mid
    
    if sum_trees >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)