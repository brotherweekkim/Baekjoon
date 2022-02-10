A = int(input())
B = int(input())
C = int(input())
cnt_list = [0]*10
num = A*B*C
while num > 0:
    cnt_list[num%10] += 1
    num //= 10
for cnt in cnt_list:
    print(cnt)

