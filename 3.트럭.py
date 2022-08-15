from collections import deque
import sys
import copy
n, w, L = map(int, input().split()) # 5 100 1000
truck = deque(list(map(int, input().split()))) # 32 500 324 7 990

answer = 1
bridge = deque([])
time = deque([])
while True:
    for i in range(len(time)):
        time[i] = time[i]+1        
    
    if len(time)>0 and time[0] > w:
        bridge.popleft()
        time.popleft()
            
    if len(truck)>0:
        if len(bridge)+1 <= w and sum(bridge)+truck[0] <= L:
            mytruck = truck.popleft()
            bridge.append(mytruck)
            time.append(1)    


    if len(bridge)==0 and len(truck)==0:
        break
    answer += 1
print(answer)
# time = 1
# cnt = 1
# weight = truck.popleft() # 32
# tmpTruck = deque([weight])
# if len(truck) == 0:
#     print(time+w)
#     sys.exit()

# while truck:  
#     a = truck.popleft() # 990
#     if cnt+1 > w or weight+a>L: # 2대>100대
#         cnt = 0
#         weight = 0                
#         time = time+ (len(tmpTruck)-1+w)
#         truck.appendleft(a)

#         checkdupl = copy.deepcopy(truck)
#         tweight = 0
#         while tmpTruck: # 32 500 324  7
#             tmptwe = checkdupl.popleft()
#             tweight += tmptwe
#             lastTruck = tmpTruck.popleft() # 32 빠짐  500 324 7 
#             if len(tmpTruck) == 0:
#                 break                        
#             if sum(tmpTruck) + tweight <= L and len(tmpTruck)+1<=w:
#                 #print(tweight)
#                 time -= 1   
#             else:
#                 checkdupl.appendleft(tweight)    
#                 #tweight -= tmptwe
#                 tweight = 0
#             if len(checkdupl) == 0:
#                 break                   
            
#         tmpTruck = deque([])
#         continue
    
#     cnt += 1
#     weight += a
#     tmpTruck.append(a)    
#     if len(truck) == 0:               
#         time = time+ (len(tmpTruck)-1+w)     
# print(time)