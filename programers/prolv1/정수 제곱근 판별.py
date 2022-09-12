def solution(n):
    root = n ** (1/2)
    if root == int(root):
        return (root + 1) ** 2
    return -1