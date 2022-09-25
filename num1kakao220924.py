today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
def solution(today, terms, privacies):
    answer = []
    today = list(today)
    day = []
    day.append(int(today[0]+today[1]+today[2]+today[3]))
    day.append(int(today[5]+today[6]))
    day.append(int(today[8]+today[9]))
    for i in range(len(terms)):
        terms[i] = list(terms[i].split())
    for i in range(len(privacies)):
        arr = list(privacies[i].split())
        end = []
        for j in terms:
            if arr[1] == j[0]:
                tmp = list(arr[0])
                end.append(int(tmp[0]+tmp[1]+tmp[2]+tmp[3]))
                end.append(int(tmp[5]+tmp[6]))
                end.append(int(tmp[8]+tmp[9]))
                end[2] += int(j[1])*28-1
                end[1] += end[2]//28
                end[2] = end[2]%28
                if end[2] == 0:
                    end[1] -= 1
                    end[2] = 28
                end[0] += end[1]//12
                end[1] = end[1]%12
                if end[1] == 0:
                    end[0] -= 1
                    end[1] = 12
        flag = False
        for k in range(3):
            if end[k] < day[k]:
                flag = True
                break
            elif end[k] > day[k]:
                break
        if flag == True:
            answer.append(i+1)
    return answer
print(solution(today, terms, privacies))