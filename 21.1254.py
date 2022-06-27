from collections import deque
arr = deque(list(input()))
tmp = deque([])
def check(graph):
    flag = False
    for i in range(len(graph)//2):
        if graph[i] != graph[-i-1]:
            flag = True
            break
    if flag == True:
        return True
    else:
        return False
def plus():
    if check(arr) == True:
        for i in range(len(arr)):
            tmp.appendleft(arr[i])
            if check(arr+tmp) == False:
                break
plus()
print(len(arr+tmp))