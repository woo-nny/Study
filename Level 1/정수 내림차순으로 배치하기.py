def solution(n):
    n=list(str(n))

    n.sort(reverse=True)

    answer =""
    for i in range(0,len(n)):
        answer += n[i]
    return int(answer)