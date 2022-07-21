from collections import deque 

N, M, V = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(N + 1)]

q = deque()
D_visited = [0] * (N + 1)
B_visited = [0] * (N + 1)

def DFS(V):
    D_visited[V] = 1
    print(V, end = " ")
    for i in range(1, N + 1):
        if D_visited[i] == 0 and arr[V][i] == 1:
            DFS(i)
    return

def BFS(V):
    q.append(V)
    B_visited[V] = 1
    while q:
        a = q.popleft()
        print(a, end =" ")
        for i in range(1, N + 1):
            if B_visited[i] == 0 and arr[a][i] == 1:
                q.append(i)
                B_visited[i] = 1

for _ in range(M):
    s, e = map(int, input().split())
    arr[s][e] = arr[e][s] = 1

DFS(V)
print()
BFS(V)
