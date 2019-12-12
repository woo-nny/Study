def solution(a, b):
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    mon_num = [31,29,31,30,31,30,31,31,30,31,30,31]
    sum =0
    for i in range(0,a-1):
        sum += mon_num[i]

    sum += b

 
    return day[sum%7-1]