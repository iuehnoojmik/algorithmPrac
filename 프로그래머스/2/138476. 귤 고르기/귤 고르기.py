def solution(k, tangerine):
    answer = 0
    dic = {}
    
    for t in tangerine:
        if t in dic:
            dic[t] += 1            
        else:
            dic[t] = 1
            
    new_dict = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    
    for key in new_dict.keys():
        k -= new_dict[key]
        answer += 1
        if k>0:
            continue
        else:
            break 
            
    return answer