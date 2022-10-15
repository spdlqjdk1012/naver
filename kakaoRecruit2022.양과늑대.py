import sys
def recur(v, adj, info, sheep, wolf, visited, nodes):
    global result
    nextnode = list(set(nodes + adj[v])) # [0,1,8]
    # [0,1,8] + [2,4] = [0,1,2,4,8]
    if info[v] == 0:
        sheep += 1
    elif info[v] == 1:
        wolf += 1

    if sheep <= wolf:
        return 
    
    for n in nextnode:
        if not visited[n]:
            visited[n] = 1
            recur(n, adj, info, sheep, wolf, visited, nextnode)
            visited[n] = 0
    result = max(result, sheep)    

def solution(info, edges):
    global result, adj
    result = 1
    # [ [1,8], [2,4]...] 자식노드만 넣는다
    adj = [[] for _ in range(len(info))]
    visited = [0 for _ in range(len(info))]
    visited[0] = 1
    for i, j in edges:
        adj[i].append(j)

    recur(0, adj, info, 0, 0, visited, [0])   
    print(result) 
    return result

solution([0,0,1,1,1,0,1,0,1,0,1,1], 
    [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])


"""
https://school.programmers.co.kr/learn/courses/30/lessons/92343/solution_groups?language=python3

1번노드까지 봄(0->1)
0 1 2 4 8 (현재 내가1을 보고 있을때 기존[1,8]+새[2,4])
T T F F F (방문한1은 더이상 보지않고 2,4,8 케이스를 진행)

0->1->2
0 1 2 4 8
T T T F F

0->1->2->4
[0, 1, 2, 3, 4, 6, 8]
 T  T T  F  F F  F

0->1->2->4->8
[0, 1, 2, 3, 4, 6, 8]  늑대가 더 많음
 T  T T  F  F F  T
....
"""