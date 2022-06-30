# https://www.acmicpc.net/problem/1174
from collections import deque
N = int(input())
arr = [0,1,2,3,4,5,6,7,8,9]
snum = []
def bfs():
    dq = deque([0,1,2,3,4,5,6,7,8,9])        
    while dq:
        n = dq.popleft()
        snum.append(n)
        if n == 0:
            continue
        
        for i in range(len(arr)):
            tmp = list(str(n))            
            tmpnum = int(tmp[-1])
            if tmpnum>arr[i]:
                dq.append( int(str(n)+str(arr[i])) )
            else:
                break
bfs()
try:
    print(snum[N-1])
except:
    print(-1)
"""
N = int(input())
sNum = [0,1,2,3,4,5,6,7,8,9]
arr = [0,1,2,3,4,5,6,7,8,9]
visited = [False] * 10
result = []

def dfs(depth, start):
    if depth == 11:
        return
    sNum.append("".join(result))
    for i in range(len(arr)):
        if visited[i]:
            continue
        visited[i] = True
        result.append(arr[i])
        dfs(depth+1, i)
        visited[i] = False
        result.pop()

dfs(0, 0)
print(sNum)
"""
"""
import sys
N = int(input())
cnt = 0

def check(num):
    flag = True
    nlist = list(str(num))
    
    before = nlist[0]
    for i in range(1, len(nlist)):
        if before <= nlist[i]:
            flag = False
            break
    return flag
for i in range(99999999):
    if check(i) is True:
        cnt += 1
    if cnt == N:
        print(i)
        sys.exit()
print(-1)
"""