def solution(n):
    n = n-1
    a=0
    b=1
    c=0
    while True:
        n -= 1
        c = a+b
        if n!=0:
            a=b
            b=c
        else:
            break
    return c%1234567