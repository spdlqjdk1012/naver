from collections import deque
N, K, P, x = input().split()
maximum = list(N)
length = int(K)
X = deque(list(x))
number = [
    [1, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1]
]
for i in range(len(X)):
    X[i] = int(X[i])
for _ in range(length-len(X)):
    X.appendleft(0)
cnt = [[0]*10 for _ in range(10)]
def count(num):
    for i in range(10):
        for j in range(7):
            if number[num][j] != number[i][j]:
                cnt[num][i] += 1
for i in range(10):
    count(i)
result = ""
total = 0
def dfs(depth, cntnum):
    global result
    global total
    if depth == length:
        if 0 < int(result) <= int(N) and int(result) != int(x):
            total += 1
        return
    for i in range(10):
        if cntnum + cnt[X[depth]][i] <= int(P):
            arr = result
            result += str(i)
            dfs(depth+1, cntnum+cnt[X[depth]][i])
            result = arr
if length-len(maximum) >= 0:
    dfs(length-len(maximum), 0)
else:
    dfs(0, 0)
print(total)