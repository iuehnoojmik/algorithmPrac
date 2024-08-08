def solution(s):
    
    if len(s) != 4:
        if len(s) != 6:
            return False
    
    if s.isdecimal() == False:
        return False
    else: 
        return True