def solution(n, m):
    orin,orim = n,m
    while True:
        remainder = m%n
        if remainder == 0:
            gcd =n
            break
        else:
            m , n = n, remainder
    lcm = (orin*orim)//gcd
    return [gcd,lcm]