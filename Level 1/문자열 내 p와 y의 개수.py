def solution(s):
    s=list(s)
    countp =0
    county =0
    for i in range(0,len(s)):
        if s[i]=='p' or s[i]=='P':
            countp += 1
        if s[i]=='y' or s[i]=='Y':
            county += 1
    print('Hello Python')
    if county == countp:
        return True
    else:
        return False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.