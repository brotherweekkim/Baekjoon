import sys
input = sys.stdin.readline

N = input()
M = int(input())
wrong_btn = list(input().split())

ch = int(N)

# 100번에서 +, -로 가는 경우
answer = abs(100 - int(N))

# 1000000가지의 수를 완전 탐색
def is_exist(num):
    nums = list(str(num))
    for n in nums:
        if n in wrong_btn:
            return False
    return True

for i in range(1000001):
    if is_exist(i):
        answer = min(answer, len(str(i)) + abs(i - ch))
print(answer)