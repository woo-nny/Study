# 전체 학생의 수는 2명 이상 30명 이하입니다.
# 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며,
#  남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

n = 5
lost = [2,4]
reserve = [3]

student=list(range(1,n+1))
answer =0

for a in list(lost):
    if a in reserve:
        reserve.remove(a)
    if a+1 in reserve:
        answer += 1
        student.remove(a)
        lost.remove(a)
    else:
        student.remove(a)
answer += len(student)
print(answer)
