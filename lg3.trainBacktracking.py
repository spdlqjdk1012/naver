# 2022 LG유플러스 개발자 채용 챌린지
a = []
dirs = []
arr = [] # [[E,S,S], [E,E,W], [N,N,W]]
ans = 100000000
dist = dict() # 비어있는 딕셔너리 생성

def toward(x): # (0,0) E:0  (1,1) E:0->(2,1) (2,1) W:2->(1,1)
    global a   
    global dirs
    # a = [[0, 1, 1], [0, 0, 2], [3, 3, 2]]
    d = a[x[1]][x[0]] # 현재 좌표가 동서남북 중 어디인지 숫자로
    return (x[0]+dirs[d][0], x[1]+dirs[d][1]) # 마주보고 있는 좌표 확인

def isFacing(x, y): # x:(1,1) y:(2,1)
    return toward(x)==y and toward(y)==x # x:E y:w 

def detect():
    global arr # [[E,S,S], [E,E,W], [N,N,W]]
    # 마주보는 모든 좌표를 저장한다
    facing, hash = [], 0
    for yy in range(len(arr)):
        for xx in range(len(arr[0])):
            # hash = (hash << 2) | a[i][j]
            # a의 배열: 0,1,2,3 4가지 조합 4진법
            hash = (hash*4) + a[yy][xx] #4진법으로 변환
            ni, nj = toward((xx, yy)) # 현재좌표와 마주보고 있는지 비교해야할 좌표
            if ni<0 or nj<0 or ni>=len(arr[0]) or nj>=len(arr):
                continue
            if isFacing((xx, yy), (ni, nj)):
                facing.append((xx, yy))
    return facing, hash

def backtracking(cnt):
    global ans
    candidates, hash = detect()
    # 마주보는 사람이 없음
    if not candidates:
        ans = min(ans, cnt)


    # 더 빠르게 온 적 있음 (더이상 볼 필요 없음)
    if dist.get(hash, 10000000) <= cnt:
        return
    dist[hash] = cnt
    # 지금까지 6번 변경했는데 여전히 마주보는 애들이 3쌍(6개) 
    # 최소 3번은 더 변경해야함 6+3 이 현재 ans보다 적어야 더 탐색할 가치가 있다 
    if cnt+len(candidates) // 2 >= ans:
        return

    for i, j in candidates:
        for turn in range(4): #->   0밑/1<- /2위 / x3->
            # (0+1)%4=1 E->S  (1+1)%4=2 S->W (2+1)%4=3 W->N (3+1)%4=0 N->E
            a[j][i] = (a[j][i]+1) % 4 
            if turn != 3: # 자기자신으로 돌아오는 경우 제외
                #0, 1 ->1   2->2
                v = 1 if turn != 1 else 2 # 위 ->  아래 <-    if turn != 2: v=1 / else: v=2
                backtracking(cnt+v)

def solution(train):   # ["ESS", "EEW", "NNW"]  
    global a 
    global dirs 
    global ans
    for i in train:
        arr.append(list(i))  # # [[E,S,S], [E,E,W], [N,N,W]]
    mappings = {'E':0, 'S':1, 'W':2, 'N':3}
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # [[0, 1, 1], [0, 0, 2], [3, 3, 2]]
    a = [ [mappings[j] for j in i] for i in arr]            
    backtracking(0) # 0번 돌림
    print(ans)
       
    return ans

solution(["ESS", "EEW", "NNW"])
#solution(["EW", "EW", "EW"])
#solution(["NSN", "ESW", "ENW", "NNN"])

"""
[E] = [오른쪽옆 x+1: W]
[W] = [왼쪽옆 x-1: E]
[N] = [위 y-1: S]
[S] = [아래 y+1: N]


1)마주보는걸 찾는다 (둘중에 하나를 변경해야함)
2)마주보고 있는애 둘중에 하나방향을 바꾼다  (2x2)
-N =>  S(y-1)->N.. y-1.. 막혀있네  카운팅 2번
-W =>   E(x-1)  , W ....  카운팅
-S => ... 

2)마주보고 있는애 둘중에 하나방향을 바꾼다  (3x2)
-N =>  S(y-1)->N.. y-1.. 막혀있네  카운팅 2번
-W =>   E(x-1)  , W ....  카운팅
-S => ... 


바꾼방향으로 마주보고 있는애가 있는지 확인한다
마주보고 잇으면 걔도 바꾼다..
반복해서 
몇번바뀐지 본다
"""