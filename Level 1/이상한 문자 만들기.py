def solution(s):
    s=s.split(' ')
    s1 = [""]*len(s)
    for i in range(0,len(s)):
        for j in range(0,len(s[i])):
            if j%2 == 0:
                s1[i] += s[i][j].upper()
            else:
                s1[i] += s[i][j].lower()
    return " ".join(s1)

   