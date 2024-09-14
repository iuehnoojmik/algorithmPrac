def solution(people, limit):
    people.sort()
    answer = 0
    left = 0
    right = len(people) - 1
    
    while left <= right:
        if left == right:
            answer += 1
            break
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
    
    return answer