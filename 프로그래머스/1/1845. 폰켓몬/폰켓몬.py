def solution(nums):
    
    count = len(nums)//2
    a = set(nums)
    
    if len(a)>count:
        return count
    else:
        return len(a)
