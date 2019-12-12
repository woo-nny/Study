def solution(s):
    count =0
    if len(s)%2 !=0 or s[0] == ")":
        return False
    for i in range(0,len(s)):
        if s[i] =='(':
                count += 1
        elif s[i]==')':
                count -= 1
        if count <0:
            return False
    if count ==0:
        return True
    elif count !=0:
        return False
# return 위치 확인