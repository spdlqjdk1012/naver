# https://www.acmicpc.net/problem/3151
import sys
N = int(input())
arr = list(map(int , sys.stdin.readline().split()))
arr.sort()
answer = 0

for i in range(N-2): # [-6 -5 -4 -4 0 1 2 2] 3 7
    # *-6 (-5) -4 -4 0 1 2 2 3 [7]
    total = -arr[i]
    left = i+1 
    right = N-1 
    check = N-1   # 맨 끝 숫자
    while left < right:
        tmp = arr[left] + arr[right]
        if total == tmp:            
            if arr[left] == arr[right]:
                answer += (right-left)
            else:               
                if check > right:
                    check = right                 
                while check > 0 and arr[right] == arr[check]:                                                                                   
                        check -= 1                     
                answer += (right-check)
            left += 1
        else:
            if total < tmp:
                right -= 1              
            else:
                left += 1       
print(answer)     


