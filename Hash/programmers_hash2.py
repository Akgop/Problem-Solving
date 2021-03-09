def solution(phone_book):   # 데이터 개수 100만
    answer = True
    phone_book.sort()
    for i in range(1, len(phone_book)):
        if phone_book[i].startswith(phone_book[i-1]):
            answer = False
            break
    return answer


print(solution(["119", "1195524421", "11955", "97674223"]))
print(solution(["123", "456", "789"]))
