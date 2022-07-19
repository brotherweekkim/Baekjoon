N = int(input())
fif = N // 5
answer = -1
for i in range(fif, -1, -1):
    if (N - i * 5) % 3 == 0:
        answer = (N - i * 5) // 3 + i
        break
print(answer)