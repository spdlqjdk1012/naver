# https://www.acmicpc.net/problem/9081
N = int(input()) 

for i in range(N):
    word = input() # HELLO
    ascword = [] # [72, 69, 76, 76, 79]
    for i in word:
        ascword.append(ord(i))    
    #print(ascword)

    # # [72, 69, 76, {76}, 79] 뒤에서 탐색하면서 작아지는 순간을 찾자
    # HELLO -> 4 3 2 1 0    
    tmp = len(ascword)-1
    for num in range(len(ascword)-1, 0, -1):        
        if ascword[num] > ascword[num-1]:
            tmp = num-1
            break
    # tmp 에서 3도출 ascword[3] = 76
    minnum = max(ascword) # 79
    miindex = len(ascword)-1 # 4
    for num in range(tmp+1, len(ascword)):
        if ascword[tmp] < ascword[num]:        
            minnum = min(minnum, ascword[num])
            miindex = num 
    #print(miindex, ascword[miindex])
    ascword[tmp], ascword[miindex] = ascword[miindex], ascword[tmp]
    #print(ascword)
    tmpsort = sorted(ascword[tmp+1:])
    #print(ascword[0:tmp+1], tmpsort)
    result = ascword[0:tmp+1]+tmpsort    
    for i in range(len(result)):
        result[i] = chr(result[i])
    print("".join(result))

"""
12335 EHLLO
213[3]5 HELLO 맨뒷자리 35는 최대숫자가아니다 3을기준으로 잡는다 기준뒤에있는 수 중 기준보다 큰 최소값과 교환
21353 HELOL

12345 DIKNR
15[2]4[3] DRINK (243은최대가아님 기준2, 2뒷자리중 2보다크면서 가장작은수는3, 두수swap 결과 15[3]42, 새로운기준3 뒷 숫자 정렬결과 15324
15324 DRKIN

1234556 EHLSTTU
4[2]655[3]1 SHUTTLE
4[3]655[2]1
4312556 SLEHTTU    
"""
"""
# dfs로는 시간초과 발생
N = int(input()) 
flag = 0
def dfs(depth, word, visited, result, realword):
    global flag
    if flag == 2:
        return
    if depth == len(word): 
        print("".join(result))   
        if flag == 1:
            print("".join(result))       
            flag = 2

        if realword==result:
            #print("nowresult:", result, realword)
            flag = 1

        return
    overlap = 0
    for i in range(len(word)):
        if not visited[i] and overlap!=word[i]:            
            visited[i] = True
            overlap = word[i]
            result.append(word[i])
            dfs(depth+1, word, visited, result, realword)
            visited[i] = False
            result.pop()


for i in range(N):
    realword = list(input())
    word = list(sorted(realword))
    visited = [False] * len(word)
    result = []
    flag = 0
    dfs(0, word, visited, result, realword)
    if flag == 1:
        print("".join(realword))

"""