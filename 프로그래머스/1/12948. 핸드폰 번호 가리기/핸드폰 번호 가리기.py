def solution(phone_number):
    answer = ''
    
    l = len(phone_number)
    
    for i in range (l-4):
        answer += "*"

    answer += phone_number[l-4:]
    
    return answer