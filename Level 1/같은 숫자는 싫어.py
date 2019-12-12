def solution(arr):
    ans_arr =[]

    for i in range(0,len(arr)-1):
        if arr[i]!=arr[i+1]:
            ans_arr.append(arr[i])
    ans_arr.append(arr[-1])

    return ans_arr