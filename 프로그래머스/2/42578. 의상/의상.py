def solution(clothes):
    answer = 1
    clothes_dict = {}
    
    for cloth in clothes:
        if cloth[1] in clothes_dict:
            clothes_dict[cloth[1]].append(cloth[0])
        else:
            clothes_dict[cloth[1]] = [cloth[0]]
    
    for key in clothes_dict.keys():
        answer *= (len(clothes_dict[key]) + 1)
        
    return answer - 1