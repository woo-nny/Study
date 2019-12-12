def solution(arr, divisor):
    answer = []
    arr.sort()
    check = True
    for i in range (0,len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
            check = False
    if check :
        answer.append(-1)
    return answer

    # import bisect
    # bisect.insort  --> 추가하면서 sort 한다.
    # return sorted([n for n in arr if n%divisor == 0]) or [-1]