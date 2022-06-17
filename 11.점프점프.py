# https://www.acmicpc.net/problem/14248
from collections import deque
N = int(input()) # 5
arr = list(map(int, input().split()))
visited = [False] * N
S = int(input())
cnt = 1
def bfs(start):
    global cnt
    visited[start] = True
    dq = deque([])
    dq.append(start)

    while dq:
        num = dq.popleft()
        for i in [arr[num], arr[num]*-1]:
            tmpNum = num+i
            if 0<=tmpNum<N and visited[tmpNum] is False:
                visited[tmpNum] = True
                dq.append(tmpNum)
                cnt+=1
bfs(S-1)
#print(visited)
print(cnt)

