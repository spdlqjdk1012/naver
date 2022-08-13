N, M, R = map(int, input().split())
Agraph = []
for _ in range(N):
    Agraph.append(list(input().split()))
call = list(input().split())
def swap(number):
    global Agraph
    if number == "1":
        cnt = 0
        for i in Agraph:
            cnt += 1
        if cnt == N:
            for i in range(N//2):
                for j in range(M):
                    Agraph[i][j], Agraph[N-1-i][j] = Agraph[N-1-i][j], Agraph[i][j]
        else:
            for i in range(M//2):
                for j in range(N):
                    Agraph[i][j], Agraph[M-1-i][j] = Agraph[M-1-i][j], Agraph[i][j]
    elif number == "2":
        cnt = 0
        for i in Agraph:
            cnt += 1
        if cnt == N:
            for i in range(N):
                for j in range(M//2):
                    Agraph[i][j], Agraph[i][M-1-j] = Agraph[i][M-1-j], Agraph[i][j]
        else:
            for i in range(M):
                for j in range(N//2):
                    Agraph[i][j], Agraph[i][N-1-j] = Agraph[i][N-1-j], Agraph[i][j]            
    elif number == "3":
        cnt = 0
        for i in Agraph:
            cnt += 1
        if cnt == N:
            Bgraph = []
            for i in range(M):
                tmp = []
                for j in range(N):
                    tmp.append(Agraph[N-1-j][i])
                Bgraph.append(tmp)
        else:
            Bgraph = []
            for i in range(N):
                tmp = []
                for j in range(M):
                    tmp.append(Agraph[M-1-j][i])
                Bgraph.append(tmp)
        Agraph = Bgraph
    elif number == "4":
        cnt = 0
        for i in Agraph:
            cnt += 1
        if cnt == N:
            Bgraph = []
            for i in range(M):
                tmp = []
                for j in range(N):
                    tmp.append(Agraph[j][M-1-i])
                Bgraph.append(tmp)
        else:
            Bgraph = []
            for i in range(N):
                tmp = []
                for j in range(M):
                    tmp.append(Agraph[j][N-1-i])
                Bgraph.append(tmp)
        Agraph = Bgraph
    elif number == "5":
        cnt = 0
        for i in Agraph:
            cnt += 1
        if cnt == N:
            Bgraph = [[0]*M for _ in range(N)]
            call = [[0, 0], [N//2, 0], [N//2, M//2], [0, M//2]]
            for i in range(4):
                for j in range(N//2):
                    for k in range(M//2):
                        if i < 3:
                            Bgraph[call[i][0]+j][call[i][1]+k] = Agraph[call[i+1][0]+j][call[i+1][1]+k]
                        else:
                            Bgraph[call[i][0]+j][call[i][1]+k] = Agraph[call[0][0]+j][call[0][1]+k]
        else:
            Bgraph = [[0]*N for _ in range(M)]
            call = [[0, 0], [M//2, 0], [M//2, N//2], [0, N//2]]
            for i in range(4):
                for j in range(M//2):
                    for k in range(N//2):
                        if i < 3:
                            Bgraph[call[i][0]+j][call[i][1]+k] = Agraph[call[i+1][0]+j][call[i+1][1]+k]
                        else:
                            Bgraph[call[i][0]+j][call[i][1]+k] = Agraph[call[0][0]+j][call[0][1]+k]
        Agraph = Bgraph
    elif number == "6":
        cnt = 0
        for i in Agraph:
            cnt += 1
        if cnt == N:
            Bgraph = [[0]*M for _ in range(N)]
            call = [[0, 0], [0, M//2], [N//2, M//2], [N//2, 0]]
            for i in range(4):
                for j in range(N//2):
                    for k in range(M//2):
                        if i < 3:
                            Bgraph[call[i][0]+j][call[i][1]+k] = Agraph[call[i+1][0]+j][call[i+1][1]+k]
                        else:
                            Bgraph[call[i][0]+j][call[i][1]+k] = Agraph[call[0][0]+j][call[0][1]+k]
        else:
            Bgraph = [[0]*N for _ in range(M)]
            call = [[0, 0], [0, N//2], [M//2, N//2], [M//2, 0]]
            for i in range(4):
                for j in range(M//2):
                    for k in range(N//2):
                        if i < 3:
                            Bgraph[call[i][0]+j][call[i][1]+k] = Agraph[call[i+1][0]+j][call[i+1][1]+k]
                        else:
                            Bgraph[call[i][0]+j][call[i][1]+k] = Agraph[call[0][0]+j][call[0][1]+k]
        Agraph = Bgraph
for i in call:
    swap(i)
for i in Agraph:
    print(*i)