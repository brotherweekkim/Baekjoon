answer = 0
for _ in range(5):
    s, e = input().split()
    s_h, s_m = map(int, s.split(":"))
    e_h, e_m = map(int, e.split(":"))
    if s_m > e_m:
        e_h -= 1
        e_m += 60
    answer += ((e_h - s_h) * 60 + e_m - s_m)

print(answer)