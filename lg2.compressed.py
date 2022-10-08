# 2022 LG유플러스 개발자 채용 챌린지
def solution(compressed):
    arr = list(compressed)
    stack = []
    for value in arr:
        if value == ")":
            value = ""
            while True:
                popvalue = stack.pop()
                if popvalue!="(" and popvalue!=")":
                    value = popvalue+value
                if popvalue=="(":
                    popvalue = ""
                    while True:
                        if len(stack)>0 and stack[-1].isdigit():
                            popvalue = stack.pop()+popvalue
                        else:
                            break
                    value = value*int(popvalue)
                    break
            
        stack.append(value)    
    answer = "".join(stack)
    print(answer)
    return answer

solution("2(2(hi)2(co))x2(bo)")
#solution("2(3(hi)co)")
#solution("10(p)")


"""
2(2(hi)2(co)) x2(bo)
2(hihicoco) x 2(bo)
hihicocohihicoco x bobo
)
i
h
(
2
(
2

)
coco
hihi
(
2

)
bo
(
2
x
hihicocohihicoco

bobo
x
hihicocohihicoco
"""