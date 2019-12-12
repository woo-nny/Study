def solution(A,B):
    sum = 0
    for i in range(0,len(A)):
        NUM=A.pop(A.index(max(A)))*B.pop(B.index(min(B)))
        sum+=NUM

    return sum


#최솟값