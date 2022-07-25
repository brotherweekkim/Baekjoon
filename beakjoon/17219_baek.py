import sys
N, M = map(int, sys.stdin.readline().split())
password_arr = {}
for i in range(N):
    site, ps = sys.stdin.readline().split()
    password_arr[site] = ps
for i in range(M):
    site_ad = sys.stdin.readline().strip()
    print(password_arr[site_ad])
