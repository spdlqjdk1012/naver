from collections import deque
N = int(input())
result = []
def bfs():
    Npos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    q = deque([])
    q.append(["", 10])
    while q:
        arr, x = q.popleft()
        for i in range(x):
            newarr = arr + str(Npos[i])
            q.append([newarr, Npos[i]])
            result.append(int(newarr))
bfs()    
result = sorted(result)
if N < 1 or N > len(result):
    print(-1)
else:
    print(result[N-1])