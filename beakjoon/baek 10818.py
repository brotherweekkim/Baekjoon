N = int(input())
num_list = list(map(int,input().split()))
min_idx = max_idx = 0
for idx in range(N):
    if num_list[idx] > num_list[max_idx]:
        max_idx = idx
    if num_list[idx] < num_list[min_idx]:
        min_idx = idx
print(num_list[min_idx], num_list[max_idx])