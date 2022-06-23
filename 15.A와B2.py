# https://www.acmicpc.net/problem/12919
import sys

S = input()
T = input()
flag = False
def recur(t):
    global S
    # if t == S:
    #     print(1)
    #     sys.exit()

    # if len(t)<=0:
    #     print(0)
    #     sys.exit()
    global flag
    if len(t) <= len(S):
        if t == S:
            flag = True
        return
    # 맨앞 문자열이 B라면 제거후 전체문자열 뒤집기 
    if t[0] == 'B':  # BCD        -> DC
        recur(t[:0:-1]) # 처음(맨뒤)부터 인덱스1번까지(0미포함) 뒤에서 -1씩
    
    # 맨뒤에 A가 있으면 A 제거
    if t[-1] == 'A':
        recur(t[:-1])
recur(T)
print(0)

#print(T[:0:-1])
# print(T[:-1])
#print(T[0], T[-1])












""" 시간초과 코드
import sys
S = input()
B = input()

def reverse(s):
    news = ""
    for i in reversed(s):
        news += i
    return news
def recur(s):
    if s == B:
        print(1)
        sys.exit()
    if len(s) >= len(B):
        return

    news1 = s+"A"
    recur(news1)
    news2 = reverse(s+"B")
    recur(news2)    
    
recur(S)
print(0)
"""