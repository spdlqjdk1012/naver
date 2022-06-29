# https://www.acmicpc.net/problem/2251
from collections import deque
a, b, c = map(int, input().split())
visited = [[False]*(b+1) for _ in range(a+1)]
answer = [] 

def bfs(x, y):
    global a, b, c
    dq = deque([])
    dq.append((x, y))    
    visited[x][y] = True

    while dq:
        tmpx, tmpy = dq.popleft()  
        z = c - (tmpx+tmpy)     
        if tmpx == 0:
            answer.append(z)                

        for i in range(6):
            tx = tmpx
            ty = tmpy
            # x-> y
            if i == 0:
                # x1/4->y 3/5  x의1만큼옮김, y의남은물2만큼 옮김 x는 물이 1밖에 없어서 1만 가능
                tmp = min(tmpx, b-tmpy) 
                tx = tmpx - tmp
                ty = tmpy + tmp
            # x-> z
            if i == 1:   # x의 남은물  z의남은용량             
                tmp = min(tmpx, c-z)   
                tx = tmpx - tmp                         
            # y-> z
            if i == 2:   # y의 남은물  z의남은용량                          
                tmp = min(tmpy, c-z) 
                ty = tmpy - tmp                         
            
            # y-> x
            if i == 3:                
                tmp = min(a-tmpx, tmpy) 
                tx = tmpx + tmp
                ty = tmpy - tmp
            # z-> x
            if i == 4:   # x의 남은용량  , z의 남은물           
                tmp = min(a-tmpx, z)  
                tx = tmpx + tmp
            # z-> y
            if i == 5:    # y의 남은용량, z의 남은물            
                tmp = min(b-tmpy, z) 
                ty = tmpy + tmp
            
            if visited[tx][ty] is False:
                visited[tx][ty] = True
                dq.append((tx, ty))
bfs(0, 0)
print(*sorted(answer))