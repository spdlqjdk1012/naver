# 2022 LG유플러스 개발자 채용 챌린지
def solution(arr):  
    resultDict = {}
    for value in arr:
        myValue = list(map(int, list(str(value)))) # [1,2,3] [3,2,1]
        myValue.sort()        
        myValue = "".join(map(str, myValue)) # "123"
        # myValue = int("".join(map(str, myValue))) int로 변환 시 0123 체크불가로 오류        
        if myValue in resultDict:
            resultDict[myValue] = resultDict[myValue]+1 # ["123"] = 3
        else:
            resultDict[myValue] = 1 # ["0123"] = 1  ["1234"] = 2 ["123"] = 1
   
    answer = len(resultDict)    
    return answer

solution([123,234,213,432,234,1234,2341,12345,324])




#----------------------------------- 시간초과
"""
def anagram(value, group):# 1123 1213
    if len(value) != len(group):
        return False
    
    if dicTable[value] == dicTable[group]:
        return True
    else:
        return False
#anagram("21123", "21311")
def toDict(value):
    valueArr = list(value)
    valueDict = {}
    for v in valueArr:
        if v in valueDict:
            valueDict[v] = valueDict[v]+1
        else:
            valueDict[v] = 1
    return valueDict
dicTable = {}
def solution(arr):    
    for value in arr:
        dicTable[str(value)] = toDict(str(value))
    #print(dicTable)
    result = []
    for value in arr:
        if len(result) == 0:
            result.append(value)
            continue
        check = False
        for group in result:
            if anagram(str(value), str(group)):
                check = True
                break
        if check is False:
            result.append(value)
       
    answer = len(result)
    print(answer)
    return answer

solution([123,234,213,432,234,1234,2341,12345,324])
"""