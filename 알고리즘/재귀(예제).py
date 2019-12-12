def countdown(i):
    print(i)
    countdown(i-1)
#무한 반복

def countdown_answer(i):
    print(i)

    if i<=1:
        return
    else:
        countdown_answer(i-1)

countdown_answer(3)