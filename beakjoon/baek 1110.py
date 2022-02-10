N = int(input())
O_N = N
cnt=0
while 1:
    f_N = N//10
    b_N = N%10
    N = b_N*10 + (f_N+b_N)%10
    cnt += 1
    if N == O_N:
        print(cnt)
        break