def solution(n):
    num = n

    n_count= bin(n).count('1')
    ansewr = 0
    while True:
        num = num+1
        if bin(num).count('1') == n_count:
            answer = num
            break
    return answer