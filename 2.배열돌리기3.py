# https://www.acmicpc.net/problem/16935
from collections import deque
import copy
def sysout(myGraph):
    for i in myGraph:
        print(*i) # [0,1,2,3,4]

# 상하반전
def cal1():
    newGraph = deque([])
    for row in graph:
        newGraph.appendleft(row)
    return newGraph
        
# 좌우반전
def cal2():
    newGraph = []
    for row in graph:
        tmp = deque([])
        for col in row:            
            tmp.appendleft(col)
        newGraph.append(tmp)
    return newGraph

# 오른쪽으로 90도 회전
def cal3():
    global M
    global N
    global graph    
    newGraph = []
    #newGraph = [[]*M for _ in range(N)] 
    for x in range(M):
        tmp = deque([])
        for y in range(N):
            tmp.appendleft(graph[y][x])
        newGraph.append(tmp)
    M, N = N, M
    return newGraph

# 왼쪽으로 90도 회전
def cal4():
    global M # x 6
    global N # y 8
    global graph
    newGraph = []
    #newGraph = [[]*M for _ in range(N)] 
    for x in range(M): # 0~5
        tmp = deque([]) 
        for y in range(N): # 0~5            
            tmp.append(graph[y][M-1-x])
        newGraph.append(tmp)
    M, N = N, M
    return newGraph

# 1<->2 4<->3
# 1:(0x0) 2:(4x0) 3:(0x3) 4:(4x4)
def xmove(stx, sty, xmove, newGraph):
    global M # x축
    global N # y축
    for y in range(sty, sty+N//2):
        for x in range(stx, stx+M//2):            
            newGraph[y][x+xmove] = graph[y][x]
    #sysout(newGraph)

def ymove(stx, sty, ymove, newGraph):
    global M # x축
    global N # y축
    for y in range(sty, sty+N//2):
        for x in range(stx, stx+M//2):            
            newGraph[y+ymove][x] = graph[y][x]
    #sysout(newGraph)

# 1번 그룹의 부분 배열을 2번 그룹 위치로, 2번을 3번으로, 3번을 4번으로, 4번을 1번으로 이동
def cal5():
    global M # x축 8
    global N # y축 6
    newGraph = [[0]*M for _ in range(N)]
    #1번->2번     
    xmove(0, 0, M//2, newGraph)
    #3번->4번
    xmove(M//2, N//2, -M//2, newGraph)
    #2번->3번
    ymove(M//2, 0, N//2, newGraph)
    #4번->1번
    ymove(0, N//2, -N//2, newGraph)
    return newGraph

def cal6():
    global M # x축 8
    global N # y축 6
    newGraph = [[0]*M for _ in range(N)]
    #1번->4번
    ymove(0, 0, N//2, newGraph)
    #4번->3번
    xmove(0, N//2, M//2, newGraph)
    #3번->2번
    ymove(M//2, N//2, -N//2, newGraph)
    #2번->1번
    xmove(M//2, 0, -M//2, newGraph)
    return newGraph

N, M, R = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
CList = list(map(int, input().split()))
for num in CList:        
    graph=eval('cal'+str(num)+'()')
    #sysout(graph)

# graph = copy.deepcopy(cal6())


sysout(graph)


# Cal3
# MxN
# 0x5
# 0x4
# 0x3
# 0x2
# 0x1
# 0x0

# 1x5
# 1x4

# Cal 4
# MxN
# 5x0
# 5x1
# 5x2
# 5x3
# 5x4
# 5x5

# 4x0
# 4x1
# 4x2
# 4x3
# 4x4
# 4x5
