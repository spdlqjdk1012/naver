# https://www.acmicpc.net/problem/15658
N = int(input()) 
numArr = list(map(int, input().split()))
oper = list(map(int, input().split())) # + - * /

minNum= int(1e9)
maxNum = 0
flag = False
def dfs(indexNum, finalNum, oper):
    global flag
    global numArr
    global minNum
    global maxNum
    if indexNum+1 >= N: 
        if flag is False:
            minNum= finalNum
            maxNum = finalNum
            flag = True
        minNum = min(finalNum, minNum)
        maxNum = max(finalNum, maxNum)
        return

    if oper[0] > 0:
        tmp = finalNum + numArr[indexNum+1] 
        oper[0] -= 1
        dfs(indexNum+1, tmp, oper)
        oper[0] += 1

    if oper[1] > 0:
        tmp = finalNum - numArr[indexNum+1] 
        oper[1] -= 1
        dfs(indexNum+1, tmp, oper)
        oper[1] += 1

    if oper[2] > 0:
        tmp = finalNum * numArr[indexNum+1] 
        oper[2] -= 1
        dfs(indexNum+1, tmp, oper)
        oper[2] += 1

    if oper[3] > 0:
        tmp = int(finalNum / numArr[indexNum+1])
        oper[3] -= 1
        dfs(indexNum+1, tmp, oper)
        oper[3] += 1
dfs(0, numArr[0], oper)
print(maxNum)
print(minNum)


"""
[반례]
3
1 1 1
0 2 0 0
-1
-1
"""