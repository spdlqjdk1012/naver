from collections import deque
import copy
N, M, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
call = []
for _ in range(K):
    call.append(list(map(int, input().split())))
def swap(r, c, s):
    global graph
    q = deque([])
    q.append([c-s-1, r-s-1, graph[r-s][c-s-1], 1, "A"])
    while q:
        x, y, new, cnt, way = q.popleft()
        if way == "A":
            nextnew = graph[y][x]
            graph[y][x] = new
            if cnt != s*2+1:
                q.append([x+1, y, nextnew, cnt+1, "A"])
            else:
                q.append([x, y+1, nextnew, 2, "B"])
        elif way == "B":
            nextnew = graph[y][x]
            graph[y][x] = new
            if cnt != s*2+1:
                q.append([x, y+1, nextnew, cnt+1, "B"])
            else:
                q.append([x-1, y, nextnew, 2, "C"])
        elif way == "C":
            nextnew = graph[y][x]
            graph[y][x] = new
            if cnt != s*2+1:
                q.append([x-1, y, nextnew, cnt+1, "C"])
            else:
                q.append([x, y-1, nextnew, 2, "D"])            
        elif way == "D":
            nextnew = graph[y][x]
            graph[y][x] = new
            if cnt != s*2:
                q.append([x, y-1, nextnew, cnt+1, "D"])
            else:
                if s-1 != 0:
                    swap(r, c, s-1)
vis = [False]*K
tmp = []
total = []
graph = []
def dfs(depth):
    global graph
    if depth == K:
        graph = copy.deepcopy(arr)
        for i in range(len(tmp)):
            swap(tmp[i][0], tmp[i][1], tmp[i][2])
        for j in graph:
            total.append(sum(j))
        return
    for i in range(K):
        if vis[i]:
            continue
        vis[i] = True
        tmp.append(call[i])
        dfs(depth+1)
        tmp.pop()
        vis[i] = False
dfs(0)
print(min(total))