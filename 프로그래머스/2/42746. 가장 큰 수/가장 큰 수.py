def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x : x*3, reverse=True)
    
    for number in numbers:
        answer += number
        
    answer = str(int(answer))
    return answer