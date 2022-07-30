from collections import deque
import sys
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))
vis = [[False]*M for _ in range(N)]
def bfs(stx, sty, samex, samey):
    q = deque([])
    q.append([stx, sty, samex, samey])
    vis[sty][stx] = True
    xpos = [0, 0, 1, -1]
    ypos = [1, -1, 0, 0]
    while q:
        x, y, prex, prey = q.popleft()
        for i in range(4):
            tmpx = x + xpos[i]
            tmpy = y + ypos[i]
            if 0 <= tmpx < M and 0 <= tmpy < N and graph[tmpy][tmpx] == graph[y][x] and (tmpx != prex or tmpy != prey):
                if vis[tmpy][tmpx] == False:
                    vis[tmpy][tmpx] = True
                    q.append([tmpx, tmpy, x, y])
                else:
                    print("Yes")
                    sys.exit()
for i in range(N):
    for j in range(M):
        if vis[i][j] == False:
            bfs(j, i, j, i)
print("No")