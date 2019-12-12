def solution(n):
    answer = 0
    a = 2
    count = 0
    while a<=n:
        for i in range(1,a+1):
            if a%i == 0: 
                count += 1
        if count == 2:
            answer += 1
            count =0
        elif count >2:
            count = 0
        a += 1
    return answer
n=10
answer = 0
answers = []
count =0
for i in range(2,n+1):
    for j in range(1,i+1):
        if i%j == 0:
            count += 1
    if count == 2:
        answers.append(i)
        count =0
    else :
        count =0
print(len(answers))


