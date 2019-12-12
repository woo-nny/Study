s = "3people 3people me"
answer =[]
s=s.lower()
s=list(s.split())
for i in list(s):
    try:
        int(i[0])
        answer.append(i)
    except:
        i=i[0].upper()+i[1:]
        answer.append(i)
print(" ".join(answer))


#숫자는 upper해도 똑같음