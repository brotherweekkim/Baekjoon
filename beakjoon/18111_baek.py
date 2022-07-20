import sys

N, M, B = map(int,sys.stdin.readline().split())
ground = []
answer = sys.maxsize
floor = 0
for _ in range(N):
    ground += (list(map(int,sys.stdin.readline().split())))

for i in range(257):
    bag = B
    work = 0
    for j in range(N * M):
        if ground[j] < i:
            block = i - ground[j]
            bag -= block
            work += block
        else:
            block = ground[j] - i
            bag += block
            work += block * 2
    if bag >= 0:
        if answer >= work:
            answer = work
            floor = i

print(answer, floor)