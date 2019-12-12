def solution(s):
    re=sorted(s)
    answer = ''
    for i in range(len(re)-1,-1,-1):
        answer += re[i]
    return answer

#join 알아보기
