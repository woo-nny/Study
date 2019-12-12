def solution(a, b):
    sum = 0
    if a<b:
        for i in range(a,b+1):
            sum += i

    elif a>b:
        for j in range(b,a+1):
            sum += j
    elif a==b:
        for k in range(a,b+1):
            sum+= k

    return sum