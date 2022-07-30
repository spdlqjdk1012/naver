# https://www.acmicpc.net/problem/17406
import copy 

def sysout(arraytmp):
    for i in arraytmp:
        print(i)
def sysoutGraph(mygraph, txt):
    print(txt,"-----------------")
    for i in mygraph:
        print(*i)

r, c, s = map(int, input().split())
graphinit = []
graph = []
resultgraph = []
for i in range(r):
    tmp = list(map(int, input().split()))
    graph.append(tmp)    
resultgraph = copy.deepcopy(graph)
graphinit = copy.deepcopy(graph)

oper = []
for i in range(s):
    oper.append(list(map(int, input().split())))

#sysout(graph)
#sysout(oper)

def rotation(stx, sty, endx, endy):    
    # ->
    for i in range(endx, stx, -1):
        #print("x축",i)
        resultgraph[sty][i] = graph[sty][i-1]    
    #sysoutGraph(resultgraph, "->")

    # ↓
    for i in range(endy, sty, -1):        
        resultgraph[i][endx] = graph[i-1][endx]
        #print("y축",i, "x ,y", endx, i, graph[i-1][endx]) 
    #sysoutGraph(resultgraph, "↓")

    # <-
    for i in range(stx, endx): #(2,4) 2,3   
        resultgraph[endy][i] = graph[endy][i+1]    
    #sysoutGraph(resultgraph, "<-")

    # ↑    
    for i in range(sty, endy):#(1, 3) 1, 2
        resultgraph[i][stx] = graph[i+1][stx] # 2
    #sysoutGraph(resultgraph, "↑")  

def operRotation(result): # [0,1]
    global graph
    global resultgraph
    #print("result:", result)
    for num in result:
        myr, myc, mys = oper[num][0], oper[num][1], oper[num][2]        
        stx, sty = myc-mys-1, myr-mys-1 
        endx, endy = myc+mys-1, myr+mys-1
        for i in range(mys): # ????? 
            #print("start!!! ", stx+i, sty+i, endx-i, endy-i)
            rotation(stx+i, sty+i, endx-i, endy-i)
        graph = copy.deepcopy(resultgraph)

        

def checksum(mygraph):
    myresult = int(1e9)
    for i in mygraph:
        myresult = min(myresult, sum(i))        
    return myresult    

finalResult = int(1e9)
def dfs(depth, visited, result):
    global finalResult
    global graph
    global resultgraph
    global s
    if depth == s-1:
        #print("result:", result)
        operRotation(result)
        #sysoutGraph(resultgraph, "최종그래프") 
        finalResult = min(finalResult, checksum(resultgraph))
        graph = copy.deepcopy(graphinit)
        resultgraph = copy.deepcopy(graphinit)
        return
    for i in range(s):
        if visited[i]:
            continue
        visited[i] = True
        result.append(i)
        dfs(depth+1, visited, result)
        result.pop()
        visited[i] = False
        
for i in range(s): # 2
    visited = [False]*s
    visited[i] = True
    result = [i]   #[0,1] [1, 0]
    dfs(0, visited, result)

print(finalResult)