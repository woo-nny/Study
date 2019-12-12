def solution(x):
    x_num=list(str(x))
    num = []
    for i in range(0,len(x_num)):
        num.append(int(x_num[i]))

    if x%sum(num) ==0:
        return True
    else:
        return False
