num_list = [0]*9
for idx in range(0,9):
    num_list[idx] = int(input())
max_idx = 0
for idx2 in range(9):
    if num_list[idx2] > num_list[max_idx]:
        max_idx = idx2
print(num_list[max_idx])
print(max_idx+1)