# https://www.acmicpc.net/problem/1254
from collections import deque

S = deque(list(input()))

# 팰린드롬 체크
def check(S):
    for i in range(len(S)//2):
        if S[i] != S[len(S)-1-i]:# 0/3 1/2
            return False
    return True

reverseS = deque([])
if check(S) is False:
    for i in range(len(S)):
        reverseS.appendleft(S[i])
        if check(S+reverseS) is True:
            print(len(S)+len(reverseS))
            break
else:
    print(len(S))