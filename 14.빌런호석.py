# https://www.acmicpc.net/problem/22251

# 48 2 5 35 2자리수인 35숫자를 1~5개 반전시킴, 그숫자는 48이하
N, K, P, X = map(int, input().split()) 
Xtmp = X
X = str(X)
if K>len(X):
    for i in range(K-len(X)):
        X= "0"+X
X = list(str(X))
#print("X:",X)
arr = [
        [1, 1, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 1, 0],
        [1, 1, 0, 1, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1]
    ]

def compareNum(num, reverse_num):
    num = int(num)
    cnt = 0
    for n in range(7):        
        if arr[num][n] != arr[reverse_num][n]:
            cnt+=1
    return cnt

matcharr = [[] for _ in range(len(X))]
visited = [[] for _ in range(len(X))]
for i, num in enumerate(X): # 3, 5    
    cnt = 0
    for reverse_num in range(10):        
        cnt = compareNum(num, reverse_num)
        # 한자리수는 안바꾸고 나머지가 바뀌는 경우도 체크
        # 최소값 1이지만 0으로 기준을 잡고 dfs에서 자기자신을 걸러줌
        if 0<=cnt<=P: 
            #print(num, reverse_num, cnt, i)
            matcharr[i].append((reverse_num, cnt))
            visited[i].append(False)
#print(matcharr)
# print(visited)
cnt = 0
def dfs(depth, result, reverse_cnt):
    global N, K, P, X, cnt, Xtmp
    if depth == len(X):
        tmp = int("".join(result))
        if 1<=tmp <= N:
            if tmp != Xtmp:
                cnt+=1            
            #print(tmp) 
        return
    for i in range(len(matcharr[depth])):
        if not visited[depth][i] and reverse_cnt+matcharr[depth][i][1]<=P:
            visited[depth][i] = True
            result.append(str(matcharr[depth][i][0]))
            dfs(depth+1, result, reverse_cnt+matcharr[depth][i][1])
            visited[depth][i] = False
            result.pop()

dfs(0, [], 0)
print(cnt)