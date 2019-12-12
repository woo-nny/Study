def solution(n):
    sb = "수박"
    s = "수"
    answer = ''
    if n % 2 ==0:
        answer=sb*(n//2)
    else:
        answer=sb*(n//2)+s

    return answer