from collections import deque
A, B, C = map(int, input().split())
vis = [[False]*(B+1) for _ in range(A+1)]
result = []
def bfs():
    Wpos = [-2, -1, 1, 2]
    q = deque([])
    vis[0][0] = True
    q.append([0, 0])
    while q:
        Aw, Bw = q.popleft()
        if Aw == 0:
            result.append(C-Aw-Bw)
        for i in range(3):
            frflag = False
            if i == 0 and Aw != 0:
                fr = i
                frflag = True
            elif i == 1 and Bw != 0:
                fr = i
                frflag = True
            elif i == 2 and C-Aw-Bw != 0:
                fr = i
                frflag = True
            if frflag == True:
                for i in range(4):
                    to = fr + Wpos[i]
                    toflag = False
                    if 0 <= to < 3:
                        if to == 0 and Aw != A:
                            if fr == 1:
                                toflag = 0
                                move = min(Bw, A-Aw)
                                newAw = Aw + move
                                newBw = Bw - move
                            elif fr == 2:
                                toflag = 1
                                move = min(C-Aw-Bw, A-Aw)
                                newAw = Aw + move
                        elif to == 1 and Bw != B:
                            if fr == 0:
                                toflag = 0
                                move = min(Aw, B-Bw)
                                newBw = Bw + move
                                newAw = Aw - move
                            elif fr == 2:
                                toflag = 2
                                move = min(C-Aw-Bw, B-Bw)
                                newBw = Bw + move
                        elif to == 2 and C-Aw-Bw != C:
                            if fr == 0:
                                toflag = 1
                                move = min(Aw+Bw, Aw)
                                newAw = Aw - move
                            elif fr == 1:
                                toflag = 2
                                move = min(Aw+Bw, Bw)
                                newBw = Bw - move
                        if toflag == 0 and vis[newAw][newBw] == False:
                            vis[newAw][newBw] = True
                            q.append([newAw, newBw])
                        elif toflag == 1 and vis[newAw][Bw] == False:
                            vis[newAw][Bw] = True
                            q.append([newAw, Bw])
                        elif toflag == 2 and vis[Aw][newBw] == False:
                            vis[Aw][newBw] = True
                            q.append([Aw, newBw])
bfs()
print(*sorted(set(result)))