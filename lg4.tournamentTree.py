# 2022 LG유플러스 개발자 채용 챌린지
def solution(players):      
    treeSize= len(players) * 2    
    tree = [0 for i in range(treeSize)]
    
    # 단말 노드에 대진 순서 채우기 (0번노드는 쓰레기값)
    # [0, 0, 0, 0, 0, 0, 0, 0, (1, 0, 0, 1, 0, 0, 1, 0)]
    for i in range(len(players), treeSize):
        tree[i] = players[i-len(players)]
    #print(tree)

    # 나머지 대진표 채우기  
    # [0,// 1, 1, 1, 1, 1, 0, 1,// 1, 0, 0, 1, 0, 0, 1, 0]
    special = 0 # 기본 대진표에서 6번의 스페셜 매치
    for i in range(len(players)-1, 0, -1): # 7~1
        tree[i] = max( tree[i*2], tree[(i*2)+1])
        if tree[i] == 1:
            special += 1
    
    ans = special
    for i in range(len(players), treeSize):
        if tree[i] == 1: # 0인 단말노드 전부 1로 변경해보기
            continue
        cur = i # 8
        plus = 0
        while cur: # 1//2 = 0
            cur = cur // 2 # 4
            if tree[cur] == 0:
                plus += 1
            if tree[cur] == 1:
                break
        
        ans = max(ans, special+plus)  
    print(ans) 
    return ans

solution([0,0,0,0,0,0,0,0])
solution([1,0,0,1,0,0,1,0])
solution([0,0,0,1])
solution([0,1,1,0,0,1,1,0])

"""
12 34 (*5 6) 78 (910) => 매치N개
12 34 (5 6) 78 (*910) => 매치M개

0)기본매치를 센다
1)변경해야할 값 변경 (5번을 변경) , +1

상대방이 0 => 스페셜+1 => 더 위를 본다
상대방이 1 => 더이상볼필요x 

"""