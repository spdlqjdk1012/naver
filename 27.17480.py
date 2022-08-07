import copy
import sys
sys.setrecursionlimit(10000)
N = int(input())
num = list(input().split())
arr = list(input())
letter = {}
total = 0
for i in range(len(num)):
    if i%2 == 1:
        letter[num[i-1]] = int(num[i])
        total += int(num[i])
def check(start, tmp):
    global tmpLetter
    if len(tmp) == total:
        result.append(tmp)
    elif start == len(arr) or tmpLetter.get(arr[start]) == None:
        return
    elif tmpLetter[arr[start]] > 0:
        tmpLetter[arr[start]] -= 1
        check(start+1, tmp+arr[start])
tmpLetter = copy.deepcopy(letter)
result = []
for j in range(len(arr)):
    check(j, "")
    tmpLetter = copy.deepcopy(letter)
def make(made1, makeTmp, made2):
    if len(makeTmp) == 1:
        if made1+list(makeTmp)+made2 not in answer:
            answer.append(made1+list(makeTmp)+made2)
    else:
        make(made1+list(reversed(list(makeTmp)[0:len(makeTmp)//2])),
        list(makeTmp)[len(makeTmp)//2:len(makeTmp)],
        made2)
        make(made1,
        list(makeTmp)[0:len(makeTmp)//2],
        list(reversed(list(makeTmp)[len(makeTmp)//2:len(makeTmp)]))+made2)
        if len(makeTmp)%2 == 1:
            make(made1+list(reversed(list(makeTmp)[0:len(makeTmp)//2+1])),
            list(makeTmp)[len(makeTmp)//2+1:len(makeTmp)],
            made2)
            make(made1,
            list(makeTmp)[0:len(makeTmp)//2+1],
            list(reversed(list(makeTmp)[len(makeTmp)//2+1:len(makeTmp)]))+made2)
answer = []
for i in range(len(result)):
    make([], result[i], [])
print(len(answer))

# [], enienc, []
# eni/enc

# []+ine, enc, []

# [], eni, cne+[]
# ==================
# [], great, []
# gre/at

# []+erg, at, []

# [], gre, ta+[]