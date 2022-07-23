# def fibonacci(n, memo):
#     if memo[n]:
#         return memo[n]
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1, memo) + fibonacci(n-2, memo)

zero_memo = [0] * 42
one_memo = [0] * 42
zero_memo[0] = 1
one_memo[1] = 1
for i in range(2, 41):
    zero_memo[i] = zero_memo[i-1] + zero_memo[i-2]
    one_memo[i] = one_memo[i-1] + one_memo[i-2]
T = int((input()))
for _ in range(T):    
    N = int(input())
    print(zero_memo[N], one_memo[N])
