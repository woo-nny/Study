def solution(s):
    if len(s) %2 ==0:
        mid =len(s)//2
        # answer = s[mid-1:mid+1]
        return s[mid-1:mid+1]
    else:
        mid=len(s)//2
        # answer=s[mid:mid+1]
        return s[mid:mid+1]

# return str[(len(str)-1)//2:len(str)//2+1]
