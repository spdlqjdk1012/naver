# https://www.acmicpc.net/problem/16929
import sys
N, M = map(int, input().split()) # y, x
graph = []
for i in range(N):
    graph.append(list(input()))
visited = [[False]*M for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(stx, sty, nowx, nowy, color, cnt):    
    for i in range(4):
        myx = nowx+dx[i]
        myy = nowy+dy[i]
        
        if 0<=myx and myx<M and 0<=myy and myy<N:
            if cnt>=4 and myx==stx and myy==sty:
                print('Yes')
                sys.exit()
            if visited[myy][myx] is False and graph[myy][myx] == color:
                visited[myy][myx] = True
                dfs(stx, sty, myx, myy, color, cnt+1)
                visited[myy][myx] = False

# 모든 좌표를 시작지점으로 탐색을 시작하기
for tmpy in range(N):
    for tmpx in range(M):
        visited[tmpy][tmpx] = 1
        dfs(tmpx, tmpy, tmpx, tmpy, graph[tmpy][tmpx], 1)

print('No')