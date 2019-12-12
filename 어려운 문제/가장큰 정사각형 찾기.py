n=[[0,1,0,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
# n=[[0,0,1,1],[1,1,1,1]]
answer = []
for i in range(0,len(n)):
    for j in range(1,len(n[i])):
        if n[i][j-1] == 1 and n[i][j]==1:
            answer.append(1)
            answer[i] += 1
print(answer)

