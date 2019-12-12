def solution(s, n):
    answer= ''
    a=list(s)
    for i in range(0,len(a)):
        if ord(a[i]) in range(65,91):
            if ord(a[i])+n > 90:
                a[i]=chr((ord(a[i])+n - 90)+64)
            else:
                a[i]=chr(ord(a[i])+n)
        elif ord(a[i]) in range(97,123):
            if ord(a[i])+n >122:
                a[i] =chr((ord(a[i])+n-122)+96)
            else:
                a[i]=chr(ord(a[i])+n)

    answer="".join(a)
    return answer