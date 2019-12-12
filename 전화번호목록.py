phone_book = ["119", "97674223", "1195524421"]
print(phone_book[2].split(phone_book[0])[0]=='')

def solution(phone_book):
    for i in range(0,len(phone_book)):
        for j in range(0,len(phone_book)):
            if i==j:
                continue
            if phone_book[j].split(phone_book[i])[0]=='':
                return False
    return True
