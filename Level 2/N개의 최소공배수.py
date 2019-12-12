def solution(arr):
    def solution(n, m):
        num1,num2 = n,m
        while True:
            remainder = m%n
            if remainder == 0:
                n_max =n
                break
            else:
                m , n = n, remainder
        n_min = (num1*num2)//n_max
        return n_min

    count =1
    while count < len(arr):
        n_max1=solution(arr.pop(0),arr.pop(0))
        arr.append(n_max1)
    return arr[0]