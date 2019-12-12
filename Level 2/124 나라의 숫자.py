def solution(n):
    answer=""
    num="412"
    while n>0:
        an_index = n%3
        
        if n%3==0:
            n -= 1
        n=n//3
        answer = num[an_index]+answer
    return answer

#다른사람 코딩 봐보기