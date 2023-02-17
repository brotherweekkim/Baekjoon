M, N, K = map(int, input().split())
s = input().replace(" ", "")
num = input().replace(" ", "")
if s in num:
    print("secret")
else:
    print("normal")
    