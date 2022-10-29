arrow = [0 for i in range(11)] #11칸
apeach = 0
lion = 0
diff = -1
answer = []

def getlower(tmp):
    global arrow
    global answer
    for i in range(len(tmp)-1, 0, -1):
        if tmp[i] > answer[i]:  
            answer = tmp[:]
            break
        elif tmp[i] < answer[i]:
            break

def getScore(info):
    global apeach, lion, diff, answer
    apeach = 0 
    lion = 0    
    for i in range(len(info)):
        if info[i] > arrow[i]:
            apeach += (10-i)
        elif info[i] < arrow[i]:
            lion += (10-i) 
        elif info[i] == arrow[i] and info[i] > 0:
            apeach += (10-i)

    if lion > apeach:     
        if diff < lion-apeach:
            diff = lion-apeach            
            tmp = arrow[:]            
            answer = tmp
        elif diff == lion-apeach:
            tmp = arrow[:]
            getlower(tmp)            
        
        
def backTracking(idx, n, info):
    if idx == 10:
        arrow[idx] = n
        getScore(info)
        return
    
    for i in range(n+1): # 0~5
        arrow[idx] = i # 0번째에 i넣기        
        backTracking(idx+1, n-i, info)

def solution(n, info):    
    global answer
    #list = [0 for i in range(11)] #11칸    
    backTracking(0, n, info) # 0번째 자리에 5발            
    if len(answer) == 0:
        answer = [-1]
    print("=========================answer:",answer)
       
    return answer
#solution(5, [2,1,1,1,0,0,0,0,0,0,0])
#solution(1, [1,0,0,0,0,0,0,0,0,0,0])
#solution(9, [0,0,1,2,0,1,1,1,1,1,1])
#solution(10, [0,0,0,0,0,0,0,0,3,4,3])