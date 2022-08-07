# https://www.acmicpc.net/problem/17480
import copy
N = int(input())
wordarr = list(input().split())
initdict = {}
mydict = {}
word = list(input())
before = 0

for index, val in enumerate(wordarr):    
    # c 1 e 2 i 1 n 2
    if index % 2 == 0:
        before = val
    if index % 2 == 1:
        mydict[before] = int(val)        
        initdict[before] = int(val)        
result = []
def recur(idx, mydict):
    global result
    keyword = []
    for i in range(idx, len(word)):
        cnt = mydict.get(word[i])
        if cnt == None: 
            return i # 다음 문자부터 체크
        elif cnt == 0:
            return idx # 처음 검사한 문자 다음부터 체크
        else:
            mydict[word[i]] = cnt-1
            if cnt-1 == 0:
                del mydict[word[i]]
            keyword.append(word[i])
            if len(mydict) == 0:
                result.append(keyword)                                
                return idx
    return len(word)

idx = -1
for i in range(len(word)):
    if idx < i:
        mydict = copy.deepcopy(initdict)
        idx = recur(i, mydict) # 0번 
#print(result)

# enienc
answer = []
txt = []

# cword는 잘릴 문자열, rword 최종문자열, oword 남은문자열
def getNew(fword, cword, rword): # enienc

    # 문자열 길이가 1이면 return rWord
    if len(cword) == 1:        
        answer.append("".join(fword+cword+rword))
        return 

    # 반을 가른다
    splitw1 = cword[0:len(cword)//2] # [e]ni 
    splitw2 = cword[len(cword)//2:] # e[ni]

    # 반 잘린 문자열을 역순으로 rword의 append
    # 나머지 반은 고정 <- 재귀호출             
    getNew(fword+list(reversed(splitw1)), splitw2, rword)   # enc, ine
    getNew(fword, splitw1, list(reversed(splitw2))+rword)   # eni, cne
        
    if len(cword) % 2 == 1:
        splitw1 = cword[0:len(cword)//2+1] # [en]i 
        splitw2 = cword[len(cword)//2+1:] # en[i] 
        getNew(fword+list(reversed(splitw1)), splitw2, rword)   # enc, ine
        getNew(fword, splitw1, list(reversed(splitw2))+rword)   # eni, cne

# getNew(['e','n','i','e','n','c'], [])
# getNew(['n','i','e','n','c','e'], [])

for answserword in result:
    #print("단어 ------------------",answserword)
    getNew(list([]), answserword, list([]))
answer = list(set(answer))    
print(len(answer))

"""
eni/enc
e/nc
	 	 getNew() <-- cn
	  getNew() <-- e
  getNew() <- ine

=>ine+e+cn

eni/en/c
	 	 getNew() <-- c
	  getNew() <-- ne
  getNew() <- ine

"""