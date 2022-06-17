from collections import deque
n = int(input())
nlist = []
vis = [False]*n
for i in range(n):
    nlist.append(i+1)
Ai = list(map(int, input().split()))
s = int(input())
q = deque([])
q.append(s)
vis[s-1] = True
cnt = 1
while q:
    start = q.popleft()
    for i in range(2):
        if i == 0:
            way = start - Ai[start-1]
        else:
            way = start + Ai[start-1]
        if 0 < way <= n and vis[way-1] == False:
            vis[way-1] = True
            cnt += 1
            q.append(way)
print(cnt)