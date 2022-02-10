num_list = [0]*10
cnt = 0
for idx in range(10):
    num_list[idx] = int(input())
rest_list = [0] * 42
for num in num_list:
    rest_list[num%42] += 1
for rest in rest_list:
    if rest != 0:
        cnt += 1
print(cnt)